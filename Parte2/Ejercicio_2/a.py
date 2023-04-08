import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv('Parte2/Ejercicio_2/ejercicio_2.csv')

x = datos.iloc[:, 0].tolist()
y = datos.iloc[:, 1].tolist()

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

# Calculo los coeficientes de la recta y = ax + b
a = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / sum((xi - x_mean)**2  for xi in x)
b = y_mean - a*x_mean

plt.plot(x, y, 'o', color='#000080')
plt.plot(x, [a*xi+b for xi in x], color='OrangeRed')
plt.show()