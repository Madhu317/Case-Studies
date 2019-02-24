
# coding: utf-8

# In[21]:


import pandas as pd
#Reading the red wine data into dataframe called red
red = pd.read_csv('C:/Users/Madhu/Udacity-Projects/winequality-red.csv', sep = ';')
red.head()
#Number of samples and Columns
red.info()
#Number of duplicated rows 
sum(red.duplicated())
#Number of unique values in quality 
red.nunique()
#Mean density 
red.describe()


# In[20]:


#Reading the White wine data into dataframe called white
white = pd.read_csv('C:/Users/Madhu/Udacity-Projects/winequality-white.csv', sep = ';')
white.head()
#Number of samples and Columns
white.info()
#Number of duplicated rows 
sum(white.duplicated())
#Duplicate rows
dup = white[white.duplicated()]
#Number of unique values in quality 
white.nunique()


# In[35]:


import numpy as np
#Create color array for red data frame
color_red = np.repeat('red', red.shape[0])
#Create color array for white  data frame
color_white = np.repeat('white', white.shape[0])

# Add color colum to both the red and white data frames

red['color'] = color_red
white['color'] = color_white

wine = red.append(white)

wine.info()

wine.head()


# In[38]:


get_ipython().magic(u'matplotlib inline')
wine.hist(figsize = (8,8));


# In[39]:


pd.plotting.scatter_matrix(wine, figsize=(15,15));


# In[50]:


#Figuring out Group by 
wine.mean()
wine.groupby(['quality', 'color']).mean()
wine.groupby(['quality', 'color'],as_index=False).mean()
wine.groupby(['quality', 'color'],as_index=False)['pH'].mean()


# In[52]:


#Using group by to find out which qulity of wine is greater by mean
wine.groupby(['color'])['quality'].mean()


# In[66]:


# View the min, 25%, 50%, 75%, max pH values with Pandas describe
wine.describe()
# Bin edges that will be used to "cut" the data into groups
bin_edges = [2.72,3.11 ,3.21 ,3.32,4.01]
# Labels for the four acidity level groups
bin_names = ['Low', 'Medium','Moderately High','High' ]
# Creates acidity_levels column
wine['acidity_levels'] = pd.cut(wine['pH'],bin_edges,labels = bin_names)
wine.head()


# In[67]:


#Using group by to find out which qulity of wine is greater by acidity
wine.groupby(['acidity_levels'])['quality'].mean()


# In[86]:


wine['alcohol'].median()

low_alcohol = wine.query('alcohol<10.3')
high_alcohol = wine.query('alcohol>=10.3')

# ensure these queries included each sample exactly once
num_samples = wine.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() 

# get mean quality rating for the low alcohol and high alcohol groups
low_alcohol['quality'].mean()


# In[85]:


high_alcohol['quality'].mean()


# In[105]:


wine['residual sugar'].median()
low_sugar = wine[wine['residual sugar'] <3]
high_sugar = wine[wine['residual sugar'] >= 3]

# ensure these queries included each sample exactly once
num1samples = wine.shape[0]
num1samples == low_sugar['quality'].count() + high_sugar['quality'].count() 

# get mean quality rating for the low alcohol and high alcohol groups
low_sugar['quality'].mean()


# In[104]:


high_sugar['quality'].mean()


# In[106]:


mean_quality_low = low_alcohol['quality'].mean()
mean_quality_high = high_alcohol['quality'].mean()


# In[108]:


import matplotlib.pyplot as plt
# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');


# In[112]:


import seaborn as sns
sns.set_style('darkgrid')

# get counts for each rating and color
color_counts = wine.groupby(['color', 'quality']).count()['pH']
color_counts

# get total counts for each color
color_totals = wine.groupby('color').count()['pH']
color_totals

# get proportions by dividing red rating counts by total # of red samples
red_proportions = color_counts['red'] / color_totals['red']
red_proportions['9'] = 0
red_proportions
red_proportions

# get proportions by dividing white rating counts by total # of white samples
white_proportions = color_counts['white'] / color_totals['white']
white_proportions

ind = np.arange(len(red_proportions))  # the x locations for the groups
width = 0.35       # the width of the bars

# plot bars
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# title and labels
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # xtick locations
labels = ['3', '4', '5', '6', '7', '8', '9']  # xtick labels
plt.xticks(locations, labels)

# legend
plt.legend()

