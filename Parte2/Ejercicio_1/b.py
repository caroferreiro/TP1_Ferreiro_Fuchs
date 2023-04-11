import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datos = pd.read_csv('Parte2/Ejercicio_1/ejercicio_1.csv')

x = list(datos['X'].values)
y = list(datos['Y'].values) 

X = np.array([[x[i]] for i in range(0,len(x))])
Y = np.array([[y[i]] for i in range(0,len(y))])

beta = ((np.linalg.inv(np.transpose(X).dot(X))).dot(np.transpose(X))).dot(Y)

# Gráficamente:
plt.plot(x, y, 'o', color= '#2211a6')
plt.plot(x, X.dot(beta), color='#ff57ca', linewidth = 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()