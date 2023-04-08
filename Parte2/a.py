import pandas as pd
import matplotlib.pyplot as plt
#import csv

# with open('ejercicio_1.csv', 'r') as datos:
#     lector_csv = csv.reader(datos)
    # Saltar la primera fila (encabezado)
#    next(lector)
    # x = []
    # y = []
    # for fila in lector:
    #     x.append(float(fila[0]))
    #     y.append(float(fila[1]))

# plt.scatter(x, y)
# plt.show()

datos = pd.read_csv('Parte2/ejercicio_1.csv')

x = datos.iloc[:, 0].tolist()
y = datos.iloc[:, 1].tolist()

plt.plot(x, y, 'o', color='#000080')
plt.show()

