import matplotlib.pyplot as plt 

candidatos = [
    'Adriane Lopes (PP)',
    'Rose Modesto (UNIÃO)',
    'Beto Perereira (PSDB)',
    'Camila Jara (PT)',
    'Beto Figueiró (NOVO)',
    'Luso de Queiroz',
    'Ubirajara Martins (DC)'
]

votos = [140913, 131525, 115516, 41966, 10885,3108, 1067]

plt.figure(figsize=(10,6))
plt.barh(candidatos, votos, color='skyblue')
plt.xlabel('Número de Votos')
plt.ylabel('Candidatos')
plt.title("Quantidade de Votos por Candidato no 1 turno das eleições 2024")
plt.grid(axis='x', linestyle= '--', alpha=0.7)


for index, value in enumerate(votos):
    plt.text(value, index, f'{value}', va='center', ha='left')

plt.tight_layout() 
plt.show()