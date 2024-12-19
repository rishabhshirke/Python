import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
df = pd.read_csv('data.csv')

print(df.head(10))

print(df.info())

df=df.dropna()
print(df.to_string())


print(df.duplicated().to_string())
print(df.corr())