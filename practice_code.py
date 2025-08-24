import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40])
print(s)

# You can set custom indexes:
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

# Pandas DataFrame (2D data)
data = {
    "Name": ["Ali", "Sara", "John"],
    "Age": [23, 25, 22],
    "City": ["Lahore", "Karachi", "New York"]
}
df = pd.DataFrame(data)
print(df)

# Reading Data from CSV
df = pd.read_csv("data.csv")
print(df.head())   # shows first 5 rows


# Basic Operations
print(df.shape)      # rows & columns
print(df.columns)    # column names
print(df["Name"])    # select one column
print(df[["Name", "Age"]])  # select multiple columns
print(df.iloc[0])    # select first row (by index)


# Data Cleaning in pandas
data = {
    "Name": ["Ali", "Sara", "John", "Sara", None],
    "Age": [23, 25, None, 25, 30],
    "City": ["Lahore", "Karachi", "New York", "Karachi", None]
}
df = pd.DataFrame(data)
print(df)

# 1. Checking the Data
print(df.info())      # Summary of columns, types, nulls
print(df.describe())  # Stats for numeric columns
print(df.head())      # First 5 rows


# 2. Handling Missing Data
print(df.isnull())         # Shows True/False for missing
print(df.isnull().sum())   # Count missing values per column

# Drop missing rows
df_drop = df.dropna()

# Fill missing values
df_fill = df.fillna({
    "Name": "Unknown",
    "Age": df["Age"].mean(),
    "City": "Unknown"
})

# 3. Removing Duplicates
print(df.duplicated())          # Check duplicates
df_no_dup = df.drop_duplicates()

#4. Renaming Columns
df_renamed = df.rename(columns={"Name": "Full Name", "Age": "Years"})

# 5. Changing Data Types
df["Age"] = df["Age"].astype("float")   # Convert to float

# 6. Filtering Data
# People older than 24
print(df[df["Age"] > 24])

# People from Karachi
print(df[df["City"] == "Karachi"])

#7. Sorting Data
df_sorted = df.sort_values(by="Age", ascending=False)
print(df_sorted)


