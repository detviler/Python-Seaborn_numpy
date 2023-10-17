#!/usr/bin/env python
# coding: utf-8

# # Q1 Solved: Pivot in python  

# First set is importing all the required packages. So I imported Panda for "Pivot Function" imported seaborn for getting the data set "tips" which is an inbuilt data set within seaborn. Also imported numpy for any aritematic operations. All functions above

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns


# Loading the inbuilt dataset "tips" from seaborn database. Below is the code and resulted data. 

# In[4]:


sns.load_dataset('tips')


# Declaring the database tips as tips_data 

# In[7]:


tips_data = sns.load_dataset('tips')


# Then, we create  pivot table using the pivot_table function. We will write the code as follows. 
# 
# values='tip': This is the column for which we want to calculate the average tip amount.
# index='day': This is the row representing the days of the week.
# columns='sex': This is the column index, representing the gender.
# aggfunc='mean': We specify that we want to calculate the mean (average) tip amount for each combination of day and gender.

# In[8]:


pivot_table = tips_data.pivot_table(values='tip', index='day', columns='sex', aggfunc='mean')


# In[9]:


print(pivot_table)


# # Q2  Use of LOC and Boolean indexing to return the dataframe only for women who did not survived the crash and were travelling in the third class from "Titanic Database"
# 

# First loading the titanic database from seaborn

# In[10]:


titanic_data = sns.load_dataset('titanic')


# Now I am filtering the database using LOC and Boolean indexer. In below code (titanic_data['sex'] == 'female') only selects female passengers == is how we say equals in python ecosystem. Once filter is done, the second filter is (titanic_data['survived'] == 0)which means where person didn't survive. The final filter is (titanic_data['class'] == 'Third') which says the person should be from third class. 

# Note: & operator is used here so only those data will be shows where above three conditions are met which is (Female/not surived(0)/ Third Class)  

# In[11]:


filtered_data = titanic_data.loc[(titanic_data['sex'] == 'female') & (titanic_data['survived'] == 0) & (titanic_data['class'] == 'Third')]


# This will print the result 

# In[12]:


print(filtered_data)


# # Q3 Sort the tips data frame with lowest to highest Tip Percentage (Hint: You need to first create a Tip
# 

# First I need to load the data in tips and declare it as tips_data for performing further operations. 

# In[13]:


tips_data = sns.load_dataset('tips')


# Then I use the below formulae. First I create a coloum called "tip_percentage" by creating a new column. We then divide the tip amount by the total bill amount and multiply by 100 to get the percentage.

# In[14]:


tips_data['tip_percentage'] = (tips_data['tip'] / tips_data['total_bill']) * 100


# We then use data frame based on the 'tip_percentage' column using the sort_values function.

# In[15]:


sorted_tips_data = tips_data.sort_values(by='tip_percentage')


# printing the result under sorted_tips_data. 

# In[16]:


print(sorted_tips_data)


# # Q4) In the mpg dataset calculate the average weight of cars manufactured in each country. 

# First here, I will laod the dataset which is "mpg" from the database of seaborn 

# In[17]:


mpg_data = sns.load_dataset('mpg')


# Now I will calculate the average weight of the cars by country. Average is good as "mean" so I use mean function here and group by country (origin column) 

# In[18]:


Avg_weight_bycountry = mpg_data.groupby('origin')['weight'].mean()


# Now I am printing this by using the below statement. Which will show the average weight of cars manufactured in each country.

# In[20]:


print(Avg_weight_bycountry)


# # Q5 On average how much do male smokers spend in the restaurant for their food bill (excluding tips)? Your answer should be;

# Since this is an activity for database "tips" I will use the "tips" database again for this. To have a different code, I will delcare it as "tips_dataset" this time rather than calling it as tips_data" last time. This is just to differentiate and for ease of understanding. 

# In[22]:


tips_dataset = sns.load_dataset('tips')


# Now I will add my filters for male smokers which is SEX == male and smoker, "and" operator is used as I need both the condition to be true. 

# In[39]:


male_smokers_data = tips_dataset[(tips_dataset['sex'] == 'Male') & (tips_dataset['smoker'] == 'Yes')]


# Now I only use the bill value excluding the tip amount from the bill so 

# In[32]:


average_food_bill_male_smokers = (male_smokers_data['total_bill'] - male_smokers_data['tip']).mean()


# Now I use the print and also use the f keyword with {} to populate the whatever value for average_food_bill_male_smokers with a statement. This is possible using the 'f' keyword.  

# In[38]:


print(f"The average food bill for male smokers (excluding tips) is: ${average_food_bill_male_smokers:.2f}")


# In[ ]:




