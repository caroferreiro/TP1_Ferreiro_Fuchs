import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('ejercicio_1.csv')

x = list(datos['X'].values)
y = list(datos['Y'].values) 

plt.plot(x, y, 'o', color='#000080')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

