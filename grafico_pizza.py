import matplotlib.pyplot as plt 
a= (10, 20, 30)
explode= (0.1, 0, 0)
labels = ["HB20", "Gol" ,"Fusca"]
plt.pie(a, explode= explode, labels = labels, autopct='%2f%%', shadow=True)
plt.title('Carros TANANANAM  TANANAMNAM TANANAM')
plt.grid(True)
plt.show()