import matplotlib.pyplot as plt 
y = (1,2,3,4)
x = (1,4,9,16)

#plt.xlabel(u'Mês x')
#plt.ylabel(u'Quantidade de chuva y')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Meu gráfico')

#plt.plot(x,y, 'ro')
plt.plot(x, y, "mD:")

plt.show()

