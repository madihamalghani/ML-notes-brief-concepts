**Learn Pandas** while analyzing the Titanic dataset. 🚢


*Using  two  files train.cvs and test.cvs, we will analyze the data. These files are taken from Kaggle Dataset*
(given in repository with this name)

<aside>
💡

I am using Google Colab and inserting these files manually.

</aside>

# **Step 1: Load the Data**

Uploading file manually. A pop up will appear, upload these files from there

```python
from google.colab import files
uploaded = files.upload() 
#upload train.cvs
```

Uploading other file:

```

from google.colab import files
uploaded = files.upload() 
#upload test.cvs
```

Import/Load these files in pandas:

```python
import pandas as pd

# Load train and test datasets
train_file = "train.csv"  
test_file = "test.csv"

df_train = pd.read_csv(train_file)
df_test = pd.read_csv(test_file)

# Display the first few rows of the train dataset.By default 5
print(df_train.head())
```

# **Step 2: Understand the Data**

Let's explore what the dataset contains.

```python
# Check basic info
print(df_train.info())

# Check missing values
print(df_train.isnull().sum())

# Summary statistics

```

Output:

It will provide the following information:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
None
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
       PassengerId    Survived      Pclass         Age       SibSp  \
count   891.000000  891.000000  891.000000  714.000000  891.000000   
mean    446.000000    0.383838    2.308642   29.699118    0.523008   
std     257.353842    0.486592    0.836071   14.526497    1.102743   
min       1.000000    0.000000    1.000000    0.420000    0.000000   
25%     223.500000    0.000000    2.000000   20.125000    0.000000   
50%     446.000000    0.000000    3.000000   28.000000    0.000000   
75%     668.500000    1.000000    3.000000   38.000000    1.000000   
max     891.000000    1.000000    3.000000   80.000000    8.000000   

            Parch        Fare  
count  891.000000  891.000000  
mean     0.381594   32.204208  
std      0.806057   49.693429  
min      0.000000    0.000000  
25%      0.000000    7.910400  
50%      0.000000   14.454200  
75%      0.000000   31.000000  
max      6.000000  512.329200 
```

# **Data Cleaning**

## **🔹 Handling Missing Values**

Let's check how many values are missing:

```python
print(df_train.isnull().sum())

```

You can remove the column with too much null values using drop.

# **Data Exploration (EDA)**

## **1️⃣ Survival Count**

```python

df_train['Survived'].value_counts()

```

Output:

🚀 **Insight**: More people died (0) than survived (1).

```

        count
Survived	
0	        549
1	        342

dtype: int64

```

## **2️⃣ Survival Rate by Gender**

```python

df_train.groupby('Sex')['Survived'].mean()

```

🚀 **Insight**: Women had a much higher survival rate than men.(Output will prove this, no offend girls 😅) 

## **3️⃣ Survival Rate by Passenger Class**

```python

df_train.groupby('Pclass')['Survived'].mean()

```

🚀 **Insight**: 1st-class passengers had the highest survival rate.

## **4️⃣ Survival Rate by Embarkation Port**

```python

df_train.groupby('Embarked')['Survived'].mean()

```

🚀 **Insight**: People who boarded at **Cherbourg (C)** had the highest survival rate.

# **Data Visualization**

### **1️⃣ Bar Chart: Survival Count**

```python

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Survived', data=df_train)
plt.title("Survival Count")
plt.show()

```

### **2️⃣ Gender & Survival Rate**

```python
sns.barplot(x='Sex', y='Survived', data=df_train)
plt.title("Survival Rate by Gender")
plt.show()

```

### **3️⃣ Passenger Class & Survival**

```python
sns.barplot(x='Pclass', y='Survived', data=df_train)
plt.title("Survival Rate by Passenger Class")
plt.show()

```

### **4️⃣ Age Distribution (Histogram)**

```python

df_train['Age'].hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

```

# **Feature Engineering**

Before using this dataset for Machine Learning, we need to **convert categorical variables** (like "Sex" and "Embarked") into numbers.

```python

# Convert 'Sex' column to numerical (male = 0, female = 1)
df_train['Sex'] = df_train['Sex'].map({'male': 0, 'female': 1})

# Convert 'Embarked' column using one-hot encoding
df_train = pd.get_dummies(df_train, columns=['Embarked'], drop_first=True)

# Drop unnecessary columns
df_train.drop(columns=['Name', 'Ticket'], inplace=True)

# Show final dataset
print(df_train.head())

```

✅ **Now, the dataset is ready for Machine Learning!** 🚀

# **✅ Summary: What You Learned**

✔ **Loading CSV files into Pandas**

✔ **Exploring the dataset (info, missing values, statistics)**

✔ **Performing Exploratory Data Analysis (EDA)**

✔ **Visualizing the dataset (Survival by Gender, Class, Age, etc.)**

✔ **Feature Engineering (Converting categorical values for ML models)**
