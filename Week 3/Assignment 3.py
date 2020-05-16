
# coding: utf-8

# In[6]:

# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df = df.transpose()
df.head()


# In[28]:

get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt
value = df.mean()
std = df.std()


# In[29]:

# Barplot -------------------------------------------------------------
def drawplot(yval):
    

    for yer, rect in zip(yerr_, barplot.get_children()):
        h = rect.get_height()
        if ( h + yer <  yval): 
            rect.set_color(colors[2])
        if ( h - yer >  yval): 
            rect.set_color(colors[0])
        if ((h - yer <  yval) & (h + yer >  yval)): 
            rect.set_color(colors[1])

    plt.xticks(range(len(df.columns)), df.columns)
    plt.ylim(0,60000)
    
    # Removing Frame
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

# Horizontal line -------------------------------------------------------------
def drawline(yval):
    plt.gca().lines[2].remove()
    plt.axhline(yval, color = 'blue', lw = 1)

# Interactivity -------------------------------------------------------------
def onclick(event):
    drawplot(event.ydata)
    drawline(event.ydata)
    yval = event.ydata


# In[30]:

# Initialize
fig = plt.figure()
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

colors  = ['red','#efefef','blue']
yerr_ = df.sem().values*1.96
yval = 42000

barplot = plt.bar(range(len(df.columns)),
        yerr = yerr_,
        height = value,
        align = 'center',
        error_kw=dict(ecolor='gray', lw=1, capsize=5, capthick=1)) 

plt.axhline(yval, color = 'blue', lw = 1)
drawplot(yval)


# In[23]:

plt.gca().lines[2].remove()


# In[ ]:



