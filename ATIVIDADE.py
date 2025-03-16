import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/kaggle/input/brasileirao-serie-a-2006-2022/brasileirao.csv")
df_2019 = df[df["season"] ==2019]

df_2019_sorted = df_2019.sort_values(by="goals", ascending=False)


plt.figure(figsize=(12, 6))
plt.bar(df_2019_sorted["team"], df_2019_sorted["goals"], color="blue")


plt.title("Total de Gols por Time - Brasileirão 2019")
plt.xlabel("Times")
plt.ylabel("Gols Marcados")
plt.xticks(rotation=90)  
plt.grid(axis="y", linestyle="--", alpha=0.7)


plt.show()