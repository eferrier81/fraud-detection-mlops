import pandas as pd
df = pd.read_csv('data/transactions.csv', sep=';')
print(df.head(10))
print(df.info())
print(df.describe())
