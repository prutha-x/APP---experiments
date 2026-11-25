import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("customer_churn.csv")

print("First five rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

df.fillna(df.median(numeric_only=True), inplace=True)

print("\nChurn Distribution:")
print(df["Churn"].value_counts())

sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.show()

df.select_dtypes(include=np.number).hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.heatmap(df.select_dtypes(include=np.number).corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    sns.boxplot(x=df[col])
    plt.title("Outlier Detection: " + col)
    plt.show()

print("\nCleaned Dataset:")
print(df.head())
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
