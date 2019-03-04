#100 PANDAS PUZZLE

#Question 1: Import Pandas under the name pd.

import pandas as pd 

#Question 2: Print the version of pandas that has been imported.

pd.__version__

#Question 3: . Print out all the version information of the libraries that are required by the pandas library

pd.show_versions()


#Importing NumPy

import numpy as np

#Input data with labels 

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#Question 4. Create a DataFrame df from this dictionary data which has the index labels.

df = pd.DataFrame(data, index=labels)

#Question 5: Display a summary of the basic information about this DataFrame and its data.

df.info()

#Question 6:  Return the first 3 rows of the DataFrame df.

df.head(3)

#Question 7: Select just the 'animal' and 'age' columns from the DataFrame df.

df[['animal', 'age']]

# Question 8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].

df.loc[df.index[[2, 3, 7]], ['animal', 'age']]

#Question 9. Select only the rows where the number of visits is greater than 3.

df[df['visits'] > 3]

#Question 10. Select the rows where the age is missing, i.e. is NaN.


df[df['age'].isnull()]

#Question 11. Select the rows where the animal is a cat and the age is less than 3.

df[(df['animal'] == 'cat') & (df['age'] < 3)]

#Question 12:  Select the rows the age is between 2 and 4 (inclusive).


df[df['age'].between(2, 4)]

#Question 13:  Change the age in row 'f' to 1.5.

df.loc['f', 'age'] = 1.5

#Question 14. Calculate the sum of all visits (the total number of visits).

df['visits'].sum()

#Question 15.  Calculate the mean age for each different animal in df.

df.groupby('animal')['age'].mean()

#Question 16. Append a new row 'k' to df with your choice of values for each column. Then delete that row to retur the original DataFrame.


df.loc['k'] = [1.5, 'cat', 'no', 1]

df = df.drop('k')

# Question 17. Count the number of each type of animal in df.

df['animal'].value_counts()

# Question 18.  Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visit' column in *ascending* order.


df.sort_values(by=['age', 'visits'], ascending=[False, True])


# Question 19: The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be `True` and 'no' should be `False`.


df['priority'] = df['priority'].map({'yes': True, 'no': False})


#Question 20:  In the 'animal' column, change the 'snake' entries to 'python'.


df['animal'] = df['animal'].replace('snake', 'python')


# Question 21. For each animal type and each number of visits, find the mean age. In other words, each row is an animal, each column is a number of visits and the values are the mean ages (hint: use a pivot table).


df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')

# Question 22.df How do you filter out rows which contain the same integer as the row immediately above?

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})

df.loc[df['A'].shift() != df['A']]

df.drop_duplicates(subset='A')


# Question 23. how do you subtract the row mean from each element in the row?

df = pd.DataFrame(np.random.random(size=(5, 3))) 

df.sub(df.mean(axis=1), axis=0)


# Question 24.Which column of numbers has the smallest sum? (Find that column's label.)

df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))

df.sum().idxmin()


# Question 25.How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?

len(df.drop_duplicates(keep=False))

 
#  Question  26. You have a DataFrame that consists of 10 columns of floating--point numbers. Suppose that exactly 5 entries in each row are NaN values. For each row of the DataFrame, find the *column* which contains the *third* NaN value.


(df.isnull().cumsum(axis=1) == 3).idxmax(axis=1)


# Question 27. A DataFrame has a column of groups 'grps' and and column of numbers 'vals'. For example: For each *group*, find the sum of the three greatest values.

df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                    'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})


df.groupby('grp')['vals'].nlargest(3).sum(level=0)


# Question 28. A DataFrame has two integer columns 'A' and 'B'. The values in 'A' are between 1 and 100 (inclusive). For each group of 10 consecutive integers in 'A' (i.e. `(0, 10]`, `(10, 20]`, ...), calculate the sum of the corresponding values in column 'B'.

df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()


#  Question 29.** Consider a DataFrame `df` where there is an integer column 'X': # For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer). These values should therefore be `[1, 2, 0, 1, 2, 3, 4, 0, 1, 2]`. Make this a new column 'Y'.


df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

iz = np.r_[-1, (df['X'] == 0).nonzero()[0]] 
ix = np.arange(len(df))
df['Y'] = ix - iz[np.searchsorted(iz - 1, ix) - 1]


# Question 30. Consider a DataFrame containing rows and columns of purely numerical data. Create a list of the row-column index locations of the 3 largest values.

df.unstack().sort_values()[-3:].index.tolist()


# Question 31. Given a DataFrame with a column of group IDs, 'grps', and a column of corresponding integer values, 'vals', replace any negative values in 'vals' with the group mean.


def replace(group):
    val = group<0
    group[val] = group[~val].mean()
    return group

df.groupby(['grps'])['vals'].transform(replace)

# Question 32.  Implement a rolling mean over groups with window size 3, which ignores NaN value. For example consider the following DataFrame:

df = pd.DataFrame({'group': list('aabbabbbabab'),
                       'value': [1, 2, 3, np.nan, 2, 3, 
                                  np.nan, 1, 7, 3, np.nan, 8]})

a1 = df.groupby(['group'])['value']             
a2 = df.fillna(0).groupby(['group'])['value']   

b = a2.rolling(3, min_periods=1).sum() / a1.rolling(3, min_periods=1).count() 

b.reset_index(level=0, drop=True).sort_index()  
 
# Question 33.  Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers. Let's call this Series `s`.


df = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(df)), index=df)


# Question 34. Find the sum of the values in `s` for every Wednesday.

s[s.index.weekday == 2].sum() 


#  Question 35.  For each calendar month in `s`, find the mean of values.

s.resample('M').mean()


#Question 36  For each group of four consecutive calendar months in `s`, find the date on which the highest value occurred.

s.groupby(pd.TimeGrouper('4M')).idxmax()


# Question 37. Create a DateTimeIndex consisting of the third Thursday in each month for the years 2015 and 2016.


pd.date_range('2015-01-01', '2016-12-31', freq='WOM-3THU')

 

# Question 38.Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column).



df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)


# Question 39. The From\_To column would be better as two separate columns! Split each string on the underscore delimiter `_` to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame. 


tempdf = df.From_To.str.split('_', expand=True)
tempdf.columns = ['From', 'To']


# Question 40. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

tempdf['From'] = tempdf['From'].str.capitalize()
tempdf['To'] = tempdf['To'].str.capitalize()


# Question 41. Delete the From_To column from `df` and attach the temporary DataFrame from the previous questions.

df = df.drop('From_To', axis=1)
df = df.join(tempdf)


# Question 42 . In the Airline column, you can see some extra puctuation and symbols have appeared around the airline names. Pull out just the airline name. E.g. `'(British Airways. )'` should become `'British Airways'`.


df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()


# Question 43 . In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN.

# Expand the Series of lists into a DataFrame named `delays`, rename the columns `delay_1`, `delay_2`, etc. and replace the unwanted RecentDelays column in `df` with `delays`.

delays = df['RecentDelays'].apply(pd.Series)

delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]

df = df.drop('RecentDelays', axis=1).join(delays)



# Question 44. Given the lists `letters = ['A', 'B', 'C']` and `numbers = list(range(10))`, construct a MultiIndex object from the product of the two lists. Use it to index a Series of random numbers. Call this Series `s`.


letters = ['A', 'B', 'C']
numbers = list(range(10))

mul = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mul)


# Question 45. Check the index of `s` is lexicographically sorted (this is a necessary proprty for indexing to work correctly with a MultiIndex).

s.index.is_lexsorted()


# Question 46. Select the labels `1`, `3` and `6` from the second level of the MultiIndexed Series.


s.loc[:, [1, 3, 6]]


# Question 47.  Slice the Series `s`; slice up to label 'B' for the first level and from label 5 onwards for the second level.


s.loc[pd.IndexSlice[:'B', 5:]]


# Question 48. Sum the values in `s` for each label in the first level (you should have Series giving you a total for labels A, B and C).

s.sum(level=0)


# Question 49. Suppose that `sum()` (and other methods) did not accept a `level` keyword argument. How else could you perform the equivalent of `s.sum(level=1)`?

s.unstack().sum(axis=0)


# Question 50 . Exchange the levels of the MultiIndex so we have an index of the form (letters, numbers). Is this new Series properly lexsorted? If not, sort it.


ns = s.swaplevel(0, 1)

ns.index.is_lexsorted()

ns = new_s.sort_index()


