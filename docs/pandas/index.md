# Pandas summary

See the [Kaggle quick tutorial on pandas](https://www.kaggle.com/learn/pandas).

Pandas has two core objects: the DataFrame and the Series.

DataFrame is like a table which contains an array of individual entries, 
each of which has a certain value. Each entry corresponds to a row (or record) and a column.

Series is a sequence of data values, it may be a single column of a DataFrame.

Here is a quick summary of some of the tutorial content:

```python
# use pandas
import pandas as pd
# Create a data frame from a dictionary whose keys are the column names and values are list of entries
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
# with row header as index
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
# read from file
home_data = pd.read_csv(a_file_path,index_col=0)
# get row / columns size
home_data.shape
home_data.head()
# Series
pd.Series(["4 cups", "1 cup", "2 large", "1 can"],index=["Flour", "Milk", "Eggs", "Spam"],name="Dinner")

```

## Indexing

Pandas uses two approach:

* **index-based selection**: To select first row of a data frame: `reviews.iloc[0]`. 
To get a column with iloc use: `reviews.iloc[:, 0]`. We can select row too, like getting 
the last five elements of the dataset: `reviews.iloc[-5:]`
* **label-based selection.** gets from data index value, not its position: `reviews.loc[0, 'country']`. 
Or select three columns and all rows: `reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]` 

Label-based selection derives its power from the labels in the index. We can set index with:

```python
reviews.set_index("title")

# Select elements that match condition 
reviews.loc[reviews.country == 'Italy']
# or within a list
reviews.loc[reviews.country.isin(['Italy', 'France'])]
# not empty cell
reviews.loc[reviews.price.notnull()]
# get specific rows
sample_reviews = reviews.iloc[[1,2,3,5,8],:]
# Combining conditions
top_oceania_wines = reviews.loc[reviews.country.isin(['New Zealand','Australia']) & (reviews.points >= 95)]
```

```python
# Get high-level summary of the attributes of the given column
reviews.points.describe()
# Get unique elements in a column
reviews.taster_name.unique()
# To see a list of unique values and how often they occur in the dataset
reviews.taster_name.value_counts()
# Ex bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
```

## map

Map() takes one set of values and "maps" them to another set of values. `map()` should expect
 a single value from the Series and return a transformed version of that value.

```python
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
# build a series to count how many times each of tropical, fruity words appears in the description column in the dataset.
topic= reviews.description.map(lambda d: "tropical" in d).sum()
fruit= reviews.description.map(lambda d: "fruity" in d).sum()
descriptor_counts = pd.Series([topic,fruit], index=['tropical', 'fruity'])
```

`apply()` transforms a whole DataFrame by calling a custom method on each row.

Both methods don't modify the original data they're called on.

## Grouping

Use `groupby()` to group our data, and then do something specific to the group the data is in:

```shell
# Group of reviews which allotted the same point values to the given wines. 
# Then, for each of these groups, grab the `points` column and count how many times it appeared
reviews.groupby('points').points.count()
# Apply transformation to the new dataframe
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
```

`agg()` lets us run a bunch of different functions on our DataFrame simultaneously

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

groupby combined with some specific operations may create [multi-indexes](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html), which looks like
a tiered structure.

```python
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
# sort by ascending
countries_reviewed.sort_values(by='len', ascending=False)
# To sort by index values, use the companion method sort_index()
# sort by more than one column
countries_reviewed.sort_values(by=['country', 'len'])
# most wine reviewer, using their twitter name
reviews.groupby(['taster_twitter_handle']).taster_twitter_handle.count()
# What is the best wine I can buy for a given amount of money? 
best_rating_per_price = reviews.groupby('price').points.max().sort_index()
# What are the minimum and maximum prices for each variety of wine? 
price_extremes = reviews.groupby('variety').price.agg([min,max])
# What are the most expensive wine varieties?
sorted_varieties = reviews.groupby('variety').price.agg([min,max]).sort_values(by=['min','max'],ascending=False)
# A series with index is reviewers and whose values is the average review score given out by that reviewer.
reviewer_mean_ratings = reviews.groupby(['taster_name']).points.agg('mean')
```

## Data types

```python
# Get data type of the points column
reviews.points.dtype
# All column types
reviews.dtypes
# convert to another type, when it makes sense
reviews.points.astype('float64')
```

## Missing values

Entries missing values are given the value NaN, short for "Not a Number". 

```python
reviews[pd.isnull(reviews.country)]
# How many reviews in the dataset are missing a price?
missing_prices = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_prices)

# What are the most common wine-producing regions? 
# Series counting the number of times each value occurs in the region_1 field. 
# This field is often missing data, so replace missing values with Unknown. 
# Sort in descending order.
reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

# Replace a value by another
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
```

## Renaming

`rename()` lets you rename index or column values by specifying a index or column keyword parameter, respectively. 

```python
reviews.rename(columns={'points': 'score'})

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# Rename index
reindexed = reviews.rename_axis('wines',axis='rows')
```

## Combining

Pandas has three core methods for doing combining data frames. In order of increasing complexity, these are `concat(), join()`, and `merge()`.

join() lets you combine different DataFrame objects which have an index in common

```python
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')
```

The lsuffix and rsuffix parameters are necessary here because the data has the same column names in both British and Canadian datasets.