import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/kaggle/input/brasileirao-serie-a-2006-2022/brasileirao.csv")
df_2019 = df[df["season"] ==2019]

mais_gols = df_2019.sort_values(by="goals", ascending=False)


plt.figure(figsize=(12, 6))
plt.bar(mais_gols["team"], mais_gols["goals"])


plt.title("Total de Gols por Time - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Gols Marcados")
plt.xticks(rotation=90)  
plt.grid(axis="y", linestyle="--", alpha=0.7)

gols_sofridos = df_2019.sort_values(by="goals_taken", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(gols_sofridos["team"], gols_sofridos["goals_taken"], color="red")

plt.title("Total de gols sofridos por time - 2019")
plt.xlabel("Times")
plt.ylabel("Gols sofridos ")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)

pontuacao_final = df_2019.sort_values(by="points", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(pontuacao_final["team"], pontuacao_final["points"], color = "green")

plt.title("Pontuação Final dos Times")
plt.xlabel("Times")
plt.ylabel("Pontuação")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()