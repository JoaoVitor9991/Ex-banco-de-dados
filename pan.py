import pandas as pd
print(pd.__version__)

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.set_index('Passagerld')
inplace=True
print(df.head(12))