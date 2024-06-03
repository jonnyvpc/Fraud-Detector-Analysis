import pandas as pd

# Exercise 0
def exercise_0(file):
    # Read the dataset as a Pandas dataframe
    df = pd.read_csv(file)
    return df

# Exercise 1
def exercise_1(df):
    # Return the column names as a list
    return df.columns.tolist()

# Exercise 2
def exercise_2(df, k):
    # Return the first k rows from the dataframe
    return df.head(k)

# Exercise 3
def exercise_3(df, k):
    # Return a random sample of k rows from the dataframe
    return df.sample(k)

# Exercise 4
def exercise_4(df):
    # Return a list of the unique transaction types
    return df['type'].unique().tolist()

# Exercise 5
def exercise_5(df):
    # Return a Pandas series of the top 10 transaction destinations with frequencies
    return df['nameDest'].value_counts().head(10)

# Exercise 6
def exercise_6(df):
    # Return all the rows from the dataframe for which fraud was detected
    return df[df['isFraud'] == 1]

# Exercise 7
def exercise_7(df):
    # Bonus: Return a dataframe that contains the number of distinct destinations that each source has interacted with, sorted in descending order
    return df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False)

# Read the dataset
df = exercise_0('transactions.csv')
