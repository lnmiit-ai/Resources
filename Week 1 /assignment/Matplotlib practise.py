
# coding: utf-8

# In[142]:


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_excel('data.xlsx',index = [])

df

df.head()

df['Label'][0]

df1 = df[df['Label']==1]

df2 = df[df['Label']==2]

fig,axes = plt.subplots(nrows = 9,ncols = 5,figsize = (40,40))
fig.subplots_adjust(hspace = 0.5) # to adjust the height between two rows of plots 

axes = axes.ravel()    #to change the axes array into a flat 1-D array
count = 0
for i in range(10):   
    #print(y)
    for j in range(i+1,10):
        x = df1[i+1]
        x = x.tolist()
        #print(x)
        y = df1[j+1]
        y = y.tolist()
        x1 = df2[i+1]
        y1 = df2[j+1]
        x1 = x1.tolist()
        y1 = y1.tolist()
        axes[count].scatter(x,y,c='r')
        axes[count].scatter(x1,y1,c='b')
        axes[count].set_title("Feature {0} vs Feature {1}".format((i+1),(j+1)))
        axes[count].set_xlabel("Feature {0}".format((i+1)))
        axes[count].set_ylabel("Feature {0}".format((j+1)))
        count = count +1
        
 ### The result is that the top left graph gives us the best classification between two labels . 
 ### We can see a clear distinction between red and blue region. 

