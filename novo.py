import pandas as pd

# Carregar o dataset do Titanic
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Definir 'PassengerId' como índice
df.set_index('PassengerId', inplace=True)

# Exibir as 12 primeiras linhas
print(df.head(12))
print(df.columns) # para descobrir as colunas 
df.values
