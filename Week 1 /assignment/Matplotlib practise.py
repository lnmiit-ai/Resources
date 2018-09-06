import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

%matplotlib inline
df = pd.read_excel('data.xlsx',index = [])

#df

#df.head()

#df['Label'][0]

df1 = df[df['Label']==1]

df2 = df[df['Label']==2]

fig,axes = plt.subplots(nrows = 9,ncols = 5,figsize = (40,40))
fig.subplots_adjust(hspace = 0.5)

axes = axes.ravel()    #to change the axes array into a flat 1-D array
count = 0
for i in range(10):   
    #print(y)
    for j in range(i+1,10):
    #I realized we do not need to seperately assign Series to another variable and convert to a list
        axes[count].scatter(df1[i+1],df1[j+1],c='r')
        axes[count].scatter(df2[i+1],df2[j+1],c='b')
        axes[count].set_title("Feature {0} vs Feature {1}".format((i+1),(j+1)))
        axes[count].set_xlabel("Feature {0}".format((i+1)))
        axes[count].set_ylabel("Feature {0}".format((j+1)))
        count = count +1
        
 ### The result is that the top left graph gives us the best classification between two labels . 
### We can see a clear distinction between red and blue region. 
