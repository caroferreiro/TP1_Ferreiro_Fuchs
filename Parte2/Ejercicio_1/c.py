import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datos = pd.read_csv('Parte2/Ejercicio_1/ejercicio_1.csv')

# a) 
x = list(datos['X'].values)
y = list(datos['Y'].values) 

# Agrego 12 a cada valor de y:
y = [valor + 12 for valor in y]

# b)

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

a = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / sum((xi - x_mean)**2 for xi in x)
b = y_mean - a * x_mean

print(f"La ecuación de la recta es: y = {a:.4f} + {b:.4f}x")

# Gráficamente:
plt.plot(x, y, 'o', color= '#000080')
plt.plot(x, [a*xi+b for xi in x], color='OrangeRed', label='Recta de mejor ajuste')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()