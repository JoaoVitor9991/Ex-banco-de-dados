import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/kaggle/input/brasileirao-serie-a-2006-2022/brasileirao.csv")
df_2019 = df[df["season"] ==2019]
#GOLS FEITOS
mais_gols = df_2019.sort_values(by="goals", ascending=False)


plt.figure(figsize=(12, 6))
plt.bar(mais_gols["team"], mais_gols["goals"])


plt.title("Total de Gols por Time - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Gols Marcados")
plt.xticks(rotation=90)  
plt.grid(axis="y", linestyle="--", alpha=0.7)

#GOLS SOFRIDOS
gols_sofridos = df_2019.sort_values(by="goals_taken", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(gols_sofridos["team"], gols_sofridos["goals_taken"], color="red")

plt.title("Total de gols sofridos por time - 2019")
plt.xlabel("Times")
plt.ylabel("Gols sofridos ")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)


#PONTOS 
pontuacao_final = df_2019.sort_values(by="points", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(pontuacao_final["team"], pontuacao_final["points"], color = "green")

plt.title("Pontuação Final dos Times")
plt.xlabel("Times")
plt.ylabel("Pontuação")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)

empates = df_2019.sort_values(by="draw", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(empates["team"], empates["draw"], color= "red")
plt.xlabel("Times")
plt.ylabel("Empates")
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle="--", alpha=0.7)

perdido = df_2019.sort_values(by="loss", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(perdido["team"], perdido["draw"], color= "red")
plt.xlabel("Times")
plt.ylabel("Perdidos")
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle="--", alpha=0.7)

vitorias = df_2019.sort_values(by="won", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(vitorias["team"], vitorias["won"], color= "green")

plt.title("Quem teve mais vitórias 2019")
plt.xlabel("Times")
plt.ylabel("Vitórias")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)

df = pd.read_csv("/kaggle/input/brasileirao-serie-a-2006-2022/brasileirao.csv")


df_2019 = df[df["season"] == 2019]


plt.figure(figsize=(10, 6))
plt.scatter(df_2019["goals"], df_2019["won"], color="blue")


for i, time in enumerate(df_2019["team"]):
    plt.annotate(time, (df_2019["goals"].iloc[i], df_2019["won"].iloc[i]), fontsize=9, alpha=0.7)


plt.title("Relação entre Gols Marcados e Vitórias - Brasileirão 2019")
plt.xlabel("Gols Marcados")
plt.ylabel("Vitórias")
plt.grid(True, linestyle="--", alpha=0.7)

#PONTOS 
pontuacao_final = df_2019.sort_values(by="points", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(pontuacao_final["team"], pontuacao_final["points"], color = "green")

plt.title("Pontuação Final dos Times")
plt.xlabel("Times")
plt.ylabel("Pontuação")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)


plt.show()