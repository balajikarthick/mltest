import pandas as pd
df = pd.read_csv("IRIS.csv")
df.head(5)
df = df.sort(columns="Type")
df.head(5)
df.to_csv("IRIS.csv")
