#!/usr/bin/env python
# coding: utf-8

# Firstly, we import all the relevent package for the exercise. Additional package for visualization is matplotlib so we import that as well. 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[15]:


import matplotlib.pyplot as plt


# Now, I will import the dataset "mpg" as mpg_data as the data is there. 

# In[16]:


mpg_data = sns.load_dataset('mpg')


# Now, since for correlative functions, I need to have only 'numeric' data. Few Columns in such as "origin" is non-numeric which can't be shown in this visualization. So I need to filter out this from the datatype before I write the code for visualization. Below function only incudes number. 

# In[20]:


numeric_data = mpg_data.select_dtypes(include='number')


# Now I use the correlation matrics.We calculate the correlation matrix by applying the .corr()correlation matrix. The correlation matrix is a table showing how strongly pairs of variables are related

# In[21]:


correlation_matrix = numeric_data.corr()


# Now, I create the heatmap, 
# We set the figure size using plt.figure (10, 6 metrics is what I choose)
# We use sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5) to generate the heatmap. This visualization shows the correlation values in color, with warmer colors indicating positive correlations(Red) and cooler colors indicating negative correlations (Blue). The annot=True argument displays the actual correlation values on the heatmap. The cmap argument specifies the color map used for the heatmap.
# Then we name it with a title & just like print function, to show the chart, we use the plt.show function. 
# 

# In[22]:


plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Correlation Heatmap of MPG Dataset")
plt.show()


# Now I create a violin plot to better visulise the relationship between Cylinder count VS MPG miles per gallon. Basically, I wanted to check how is the MPG trending with increasing cylinder count. My rough assumption based on data reading is the MPG should go down with higher cylinder count. Now, I load the data set of mpg from the database. 
# 
# Chart Inference: This heatmap shows how well each elements are coorelated. We see that warmer colors are deeply coorelated. Which means MPG (Miles per Gallon ) fule efficency is closely impacted from the number of cylinder, displacement, hourse power and weight of the vehicle as they all are show in deep red. 
# 

# In[23]:


mpg_data = sns.load_dataset('mpg')


# Now, I create the Violin plot. figure size takes the tuple value where one is height and other is width.  where in x axis I need the cylinder count, in Y axis I need the mpg value. sns violinplot is a function in seaborn which creates the violinplot for us. pltfunction will help us label the chart. plt.show will print the result. 
# 
# Chart Inference: This visualization clearly shows, the MPV is low for 3 cylinder engines, however for most of the 4 cylinder engines the mpv is around 30 to 40 which is good. 5 cylinder engines are good too, but we don't have much data (vehicles) which is seen by the narrowness of the violin. For 6 and 8 cylinder engines, its clear the MpV is too low for most of the vehicles and only very few of them has an mpv close to 40 and 30 respectively. 

# In[27]:


plt.figure(figsize=(10, 5))
sns.violinplot(x='cylinders', y='mpg', data=mpg_data, palette='Set2')
plt.title("Violin Plot of MPG vs Cylinder Count")
plt.xlabel("Cylinder Count")
plt.ylabel("MPG")
plt.show()


# In[ ]:





# In[ ]:




