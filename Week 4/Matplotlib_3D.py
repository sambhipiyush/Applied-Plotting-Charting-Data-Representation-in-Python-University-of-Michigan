
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')


# In[2]:

iris = pd.read_csv('iris.csv')

plt.figure()

for species, irissubset in iris.groupby('Name'):
    plt.scatter(irissubset['PetalLength'], irissubset['PetalWidth'], alpha=0.8, label=species)

plt.xlabel('PetalLength')
plt.ylabel('PetalWidth')
plt.legend();


# In[3]:

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for species, irissubset in iris.groupby('Name'):
    ax.scatter(irissubset['SepalLength'], irissubset['PetalLength'], irissubset['PetalWidth'], label=species)

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Petal Length')
ax.set_zlabel('Petal Width')
ax.legend(loc=2)

plt.show()


# In[4]:

x, y, z = axes3d.get_test_data(0.1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z)

plt.show()


# In[5]:

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap = 'viridis')

plt.show()


# In[6]:

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap = 'viridis')

for angle in range(-90, 270):
    ax.view_init(90, angle)
    plt.draw()

plt.show()


# In[7]:

fig = plt.figure()
ax = fig.add_subplot(111)
x, y, z = axes3d.get_test_data(0.1)
ax.contourf(x, y, z, 100)

plt.show()


# In[ ]:



