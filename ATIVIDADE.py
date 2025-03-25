import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV uma única vez
df = pd.read_csv("/kaggle/input/brasileirao-serie-a-2006-2022/brasileirao.csv")
df_2019 = df[df["season"] == 2019]

# 1. GOLS FEITOS
mais_gols = df_2019.sort_values(by="goals", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(mais_gols["team"], mais_gols["goals"])
plt.title("Total de Gols por Time - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Gols Marcados")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()  # Ajusta o layout para evitar cortes
plt.savefig("gols_feitos_2019.png")  # Salva o gráfico
plt.close()  # Fecha a figura para liberar memória

# 2. GOLS SOFRIDOS
gols_sofridos = df_2019.sort_values(by="goals_taken", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(gols_sofridos["team"], gols_sofridos["goals_taken"], color="red")
plt.title("Total de Gols Sofridos por Time - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Gols Sofridos")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("gols_sofridos_2019.png")
plt.close()

# 3. PONTUAÇÃO FINAL
pontuacao_final = df_2019.sort_values(by="points", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(pontuacao_final["team"], pontuacao_final["points"], color="green")
plt.title("Pontuação Final dos Times - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Pontuação")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("pontuacao_final_2019.png")
plt.close()

# 4. EMPATES
empates = df_2019.sort_values(by="draw", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(empates["team"], empates["draw"], color="red")
plt.title("Total de Empates por Time - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Empates")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("empates_2019.png")
plt.close()

# 5. PERDIDOS (CORRIGIDO)
perdido = df_2019.sort_values(by="loss", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(perdido["team"], perdido["loss"], color="red")  # Corrigido: "draw" para "loss"
plt.title("Total de Derrotas por Time - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Derrotas")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("derrotas_2019.png")
plt.close()

# 6. VITÓRIAS
vitorias = df_2019.sort_values(by="won", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(vitorias["team"], vitorias["won"], color="green")
plt.title("Quem Teve Mais Vitórias - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Vitórias")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("vitorias_2019.png")
plt.close()

# 7. RELAÇÃO ENTRE GOLS MARCADOS E VITÓRIAS
plt.figure(figsize=(10, 6))
plt.scatter(df_2019["goals"], df_2019["won"], color="blue")
for i, time in enumerate(df_2019["team"]):
    plt.annotate(time, (df_2019["goals"].iloc[i], df_2019["won"].iloc[i]), fontsize=9, alpha=0.7)
plt.title("Relação entre Gols Marcados e Vitórias - Brasileirão 2019")
plt.xlabel("Gols Marcados")
plt.ylabel("Vitórias")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("relacao_gols_vitorias_2019.png")
plt.close()