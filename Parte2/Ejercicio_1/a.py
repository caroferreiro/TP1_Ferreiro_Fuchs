import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('Parte2/Ejercicio_1/ejercicio_1.csv')

x = datos.iloc[:, 0].tolist()
y = datos.iloc[:, 1].tolist()

plt.plot(x, y, 'o', color='#000080')
plt.show()

