import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datos = pd.read_csv('Parte2\ejercicio_1.csv')

# a) 
x = datos.iloc[:, 0].tolist()
y = datos.iloc[:, 1].tolist()

# Agrego 12 a cada valor de y:
y = [valor + 12 for valor in y]

plt.plot(x, y, 'o', color='#000080')
plt.show()

# b)

# x_mean = sum(x) / len(x)
# y_mean = sum(y) / len(y)

# b = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / sum((xi - x_mean)**2 for xi in x)
# a = y_mean - b * x_mean

# print(f"La ecuación de la recta es: y = {a:.4f} + {b:.4f}x")
pendiente, intercepto = np.polyfit(x, y, 1)

# Gráficamente:
plt.plot(x, y, 'o', color= '#000080')
x = np.array(x)
# plt.plot(x, a*x+b, color='OrangeRed', label='Recta de mejor ajuste')
plt.plot(x, pendiente*x + intercepto, color='OrangeRed')
plt.show()