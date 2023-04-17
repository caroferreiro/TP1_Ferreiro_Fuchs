import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('Parte3/real-estate-valuation-data-set.csv')

datos_entrenamiento = datos.iloc[0:315]
datos_test = datos.iloc[315:]

x_entrenamiento = datos_entrenamiento[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y = datos_entrenamiento[["Y house price of unit area"]]

plt.plot(x_entrenamiento, Y, 'o', color='#2211a6')
plt.xlabel('x_entrenamiento')
plt.ylabel('Y')
plt.show()

x_test = datos_test[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y_t = datos_test[["Y house price of unit area"]]
plt.plot(x_test, Y_t, 'o', color='#2211a6')
plt.xlabel('x_test')
plt.ylabel('Y')
plt.show()