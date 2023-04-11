import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv('Parte2/Ejercicio_2/ejercicio_2.csv')

x = list(datos['X'].values)
y = list(datos['Y'].values) 

X = np.array([[x[i]] for i in range(0,len(x))])
Y = np.array([[y[i]] for i in range(0,len(y))])

beta = ((np.linalg.inv(np.transpose(X).dot(X))).dot(np.transpose(X))).dot(Y)
print(beta)

plt.plot(x, y, 'o', color='#000080')
plt.plot(x, X.dot(beta), color='OrangeRed')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()