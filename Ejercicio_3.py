import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/real-estate-valuation-data-set.csv')
datos_entrenamiento = df.iloc[0:315]
datos_test = df.iloc[315:]

x_entrenamiento = datos_entrenamiento[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y = datos_entrenamiento["Y house price of unit area"].astype(float)
X_entrenamiento = np.array(x_entrenamiento)


Xe_t = np.transpose(X_entrenamiento)
Xe_t_X = np.dot(Xe_t, X_entrenamiento)
inv_Xe_t_X = np.linalg.inv(Xe_t_X)
beta_optimo = np.dot((np.dot(inv_Xe_t_X, Xe_t)), Y)

y_estimado = X_entrenamiento.dot(beta_optimo.T)
Y_estimado = np.array(y_estimado)


#valor absoluto de la diferencia entre el precio por Ping (Y) real y el estimado
diferencia = abs(Y-y_estimado)
print(list(diferencia))
 
x = list(range(0,315))

plt.plot(x, diferencia, 'o', color='#e6198a')
plt.xlabel('N° de Casa')
plt.ylabel('Error cometido')
plt.show()
