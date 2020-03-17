import pandas as pd

df = pd.read_csv("data.csv", index_col=0)

dtypes = {"POP": "float32", "AREA": "float32", "GDP": "float32"}

df = pd.read_csv("data.csv", index_col=0, dtype=dtypes, parse_dates=["IND_DAY"])
df.to_csv('formatted-data.csv', date_format='%B %d, %Y')

x = df.dtypes

print(x)

print(df)

