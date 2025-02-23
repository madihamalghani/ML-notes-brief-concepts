## Core Data Structures

Pandas mainly provides two data structures:

### **Series**

- A one-dimensional labeled array.
- Can hold data of any type (integers, strings, floating point numbers, etc.).

Example:

```python
# Creating a Series from a list
data = [10, 20, 30, 40]
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)

```

### **DataFrame**

- A two-dimensional labeled data structure with columns of potentially different types.
- Think of it as a table or spreadsheet.

Example:

```python
# Creating a DataFrame from a dictionary
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)
print(df)

```

Output:

```python
      Name  Age      City
0    Alice   25  New York
1      Bob   30     Paris
2  Charlie   35    London
```

## 3. Reading and Writing Data

Pandas makes it easy to load data from various file formats.

### **Reading Data**

- **CSV Files**
    
    ```python
    df = pd.read_csv('data.csv')
    ```
    
- **Excel Files**
    
    ```python
    
    df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    
    ```
    
- **JSON Files**
    
    ```python
    
    df = pd.read_json('data.json')
    
    ```
    

### **Writing Data**

- **To CSV**
    
    ```python
    
    df.to_csv('output.csv', index=False)
    
    ```
    
- **To Excel**
    
    ```python
    
    df.to_excel('output.xlsx', index=False)
    
    ```
    

---

## 4. Exploring and Inspecting Data

Once you load data, you need to inspect it:

- **View the first/last few rows:**
    
    ```python
    print(df.head())  # First 5 rows by default
    print(df.tail())  # Last 5 rows by default
    
    ```
    
- **Summary statistics:**
    
    ```python
    
    print(df.describe())
    
    #it will provide output like this:  
    #      Age
    #count   3.0
    #mean   30.0
    #std     5.0
    #min    25.0
    #25%    27.5
    #50%    30.0
    #75%    32.5
    #max    35.0
    ```
    
- **Data types:**
    
    ```python
    
    print(df.dtypes)
    
    ```
    
- **Info about DataFrame:**
    
    ```python
    
    print(df.info())
    
    ```
    
- **Viewing specific columns:**
    
    ```python
    print(df['Name'])            # Single column
    print(df[['Name', 'Age']])   # Multiple columns
    
    ```
    

---

## 5. Data Cleaning & Manipulation

### **Handling Missing Data**

- **Detect missing values:**
    
    ```python
    
    print(df.isnull().sum())
    
    ```
    
- **Drop missing values:**
    
    ```python
    
    df_clean = df.dropna()
    
    ```
    
- **Fill missing values:**
    
    ```python
    df_filled = df.fillna(value={'Age': df['Age'].mean()})
    
    ```
    

### **Renaming Columns**

```python
df = df.rename(columns={'Name': 'FullName', 'Age': 'Years'})

```

### **Filtering and Selecting Data**

- **Using conditions:**
    
    ```python
    
    adults = df[df['Age'] >= 18]
    
    ```
    
- **Using `.loc` and `.iloc`:**
    
    ```python
    # .loc: label-based indexing
    print(df.loc[0, 'FullName'])
    
    # .iloc: integer-based indexing
    print(df.iloc[0, 0])
    
    ```
    

### **Sorting Data**

```python

df_sorted = df.sort_values(by='Age')

```

### **Removing Duplicates**

```python

df_no_duplicates = df.drop_duplicates()

```

---

## 6. Data Transformation

### **Grouping and Aggregation**

Grouping data allows you to perform aggregate functions on subsets of your data.

```python
grouped = df.groupby('City')
print(grouped['Age'].mean())

```

### **Pivot Tables**

Pivot tables summarize data and are especially useful for multidimensional analysis.

```python
pivot_table = df.pivot_table(index='City', values='Age', aggfunc='mean')
print(pivot_table)

```

### **Merging and Joining Data**

- **Concatenating DataFrames:**
    
    ```python
    df_new = pd.concat([df1, df2])
    
    ```
    
- **Merging DataFrames on a key:**
    
    ```python
    merged_df = pd.merge(df1, df2, on='ID')
    
    ```
    
- **Joining DataFrames:**
    
    ```python
    joined_df = df1.join(df2.set_index('ID'), on='ID')
    
    ```
    

---

## 7. Time Series Data

Pandas offers extensive tools for working with time series data.

### **Converting to DateTime**

```python

df['date'] = pd.to_datetime(df['date'])

```

### **Setting DateTime as Index**

```python

df = df.set_index('date')

```

### **Resampling Data**

Aggregate data over different time periods.

```python

monthly_mean = df.resample('M').mean()

```

### **Rolling Statistics**

Calculate moving averages and other rolling statistics.

```python

df['rolling_avg'] = df['Age'].rolling(window=3).mean()

```

---

## 8. Data Visualization

Pandas integrates well with Matplotlib to create simple plots.

### **Basic Plots**

```python

import matplotlib.pyplot as plt

df['Age'].plot(kind='hist', bins=10)
plt.show()

```

Other plot types include:

- Line plots: `df.plot()`
- Bar plots: `df.plot(kind='bar')`
- Box plots: `df.boxplot()`

---