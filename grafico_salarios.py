import matplotlib.pyplot as plt 

anos = list(range(2000, 2026))
salarios = [151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510, 
            545, 622, 678, 724, 788, 880, 937, 954, 998, 1045, 
            1100, 1212, 1320, 1412, 1500]

plt.figure(figsize=(10, 5))
plt.plot(anos, salarios, marker = 'o', linestyle= '-', color='b', label= 'Salário Mínimo')

plt.xlabel('Ano')
plt.ylabel('Salário Mínimo (R$)')
plt.title("Evolução do Salário Mínimo (2000-2025)")
plt.legend()

plt.grid(True)


plt.show()