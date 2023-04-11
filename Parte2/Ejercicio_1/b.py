import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datos = pd.read_csv('Parte2/Ejercicio_1/ejercicio_1.csv')

x = list(datos['X'].values)
y = list(datos['Y'].values) 

X = np.array([[x[i]] for i in range(0,len(x))])
Y = np.array([[y[i]] for i in range(0,len(y))])

beta = ((np.linalg.inv(np.transpose(X).dot(X))).dot(np.transpose(X))).dot(Y)

# Calcular la pendiente a y el intercepto b tal que y = ax + b
pendiente, intercepto = np.polyfit(x, y, 1)
print("Pendiente:", pendiente)
print("Intercepto:", intercepto)

# Gráficamente:
plt.plot(x, y, 'o', color= '#d66eff')
plt.plot(x, X.dot(beta), color='#7902a8', linewidth = 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()