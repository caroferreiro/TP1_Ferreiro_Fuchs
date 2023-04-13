import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import sqrt
datos = pd.read_csv('Parte2/Ejercicio_1/ejercicio_1.csv')

# a) 
x = list(datos['X'].values)
y = list(datos['Y'].values) 


# Agrego 12 a cada valor de y:
y = [valor + 12 for valor in y]


# b)
X = np.array([[x[i]] for i in range(0,len(x))])
Y = np.array([[y[i]] for i in range(0,len(y))])

beta = ((np.linalg.inv(np.transpose(X).dot(X))).dot(np.transpose(X))).dot(Y)
print(beta)

# Gráficamente:
plt.plot(x, y, 'o', color= '#0aa14b')
plt.plot(x, X.dot(beta), color='#c210aa', linewidth = 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()