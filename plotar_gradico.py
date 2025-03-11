import matplotlib.pyplot as plt 
a= (1, 2, 3, 4, 5)
b = (1, 2, 3, 4, 5)
d= (2, 2, 5, 4, 5)
e = (2, 4, 3, 4, 5)

plt.subplot(1, 2, 1)
plt.plot(a, b)
plt.subplot(1, 2, 2)
plt.plot(d,e)

plt.show()