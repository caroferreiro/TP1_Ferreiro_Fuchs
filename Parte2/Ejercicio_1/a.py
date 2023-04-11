import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('Parte2/Ejercicio_1/ejercicio_1.csv')

x = list(datos['X'].values)
y = list(datos['Y'].values) 

plt.plot(x, y, 'o', color='#d66eff')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

