import pandas as pd


df = pd.read_csv("data/dataset.csv")


print("Shape of dataset:", df.shape)
print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())
