
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs to the given economy, or major changes in the economy compared to other regions.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[3]:

# Loading Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')


# In[4]:

# Monthly data
monthly = pd.read_csv('Unemployment_Rate_M_Urban.txt', sep = ',', skiprows = 1)
monthly.head()


# In[5]:

# Data Cleaning
monthly.columns = monthly.columns.str.strip()
monthly['Date'] = pd.to_datetime(monthly['Date'])


# In[6]:

# Classifying as categories
monthly['is_UT'] = 'States';
UT = ['Delhi', 'Chandigarh', 'Puducherry']
monthly.head()
monthly['is_UT'][monthly['Region'] == 'India'] = 'India Urban' ; # Classifying India Urban


# In[7]:

for key, value in monthly['Region'].items():
    if value in UT:
        monthly['is_UT'][key] = 'UTs'  


# In[8]:

monthly['Month'] = pd.DatetimeIndex(monthly['Date']).month
monthly['Year'] = pd.DatetimeIndex(monthly['Date']).year
monthly.head()


# In[9]:

monthly['is_UT'].unique()
grouped = monthly.groupby(['is_UT','Year','Month']).mean()
grouped = grouped.reset_index()


# In[10]:

import calendar
grouped['Month'] = grouped['Month'].apply(lambda x: calendar.month_abbr[x])
grouped.head()


# In[11]:

x_labels = grouped['Month'].astype(str) +  grouped['Year'].astype(str).map(lambda x: x[2:])

x_labels[:5]


# In[16]:

import seaborn as sns
fig = plt.figure()

sns.pointplot(x = x_labels, y = 'Value', hue = 'is_UT', data = grouped, palette = "colorblind", scale = 0.7, linewidth = '')

# Aesthetics
sns.set_style("white", {'font-family': [u'Arial']})
sns.set_context('notebook', font_scale=.90)

sns.despine(left = True)
plt.xlabel('Month')
plt.ylabel('Mean Unemployment Rate (%)')
plt.title('Mean Unemployment Rate of Urban population in \nIndia vs States vs UTs(Jan 16 - Jun 17)')

plt.gca().spines['bottom'].set_color('#e1e1e1')
plt.gca().spines['bottom'].set_linestyle('--')
fig.autofmt_xdate()
plt.gca().set_ylim(0,20)
plt.gca().set_yticks(range(0,20,5))
plt.gca().yaxis.grid(which = 'major', color = '#e1e1e1', linestyle = '--', linewidth = 0.5)

# Customize legend
plt.legend(title='Regions')

ylabs = plt.gca().get_yticks().astype(int).astype(str)
ylabs  = [str(x) + '%' for x in ylabs]
plt.gca().set_yticklabels(ylabs)

ylabs = plt.gca().get_yticks().astype(int).astype(str)
ylabs  = [str(x) + '%' for x in ylabs]
plt.gca().set_yticklabels(ylabs)


# In[18]:

plt.legend().get_texts()[2].set_text('UTs (Pondicherry, \nDelhi & Chandigarh)')


# In[ ]:



