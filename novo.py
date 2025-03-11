import pandas as pd

# Carregar o dataset do Titanic
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Definir 'PassengerId' como índice
df.set_index('PassengerId', inplace=True)

# Exibir as 12 primeiras linhas
print(df.head(12))
print(df.columns) # para descobrir as colunas 
df.values
df.describe #contagem, média
print(df.loc[1]) #dado do primeiro elemento
print(df.loc[[1,2,3]]) 
print(df.loc[[1,2], ['Name', 'Sex', 'Age']])
print(df.loc[10:20]) #pesquisa fatiada
print(df.loc[10:20:2])       #inicio o fim e o salto
print(df.loc[10:])                
print(df.loc[1:10, ['Name', 'Sex', 'Age']])
print(df.query('Age > 20').head())
print(df.query('Age > 20'))