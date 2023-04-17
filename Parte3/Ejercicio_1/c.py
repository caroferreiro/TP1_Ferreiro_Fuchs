import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/real-estate-valuation-data-set.csv')

datos_entrenamiento = df.iloc[0:315]
datos_test = df.iloc[315:]

x_entrenamiento = datos_entrenamiento[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y = datos_entrenamiento["Y house price of unit area"].astype(float)
# Y = np.matrix(y)
X_entrenamiento = np.matrix(x_entrenamiento)
print(Y)
# Trasponemos X:
Xe_t = np.transpose(X_entrenamiento)

# Multiplicamos Xt por X:
Xe_t_X = np.dot(Xe_t, X_entrenamiento)

# Invertimos la multiplicación anterior:
inv_Xe_t_X = np.linalg.inv(Xe_t_X)

# Calculamos el beta óptimo:
beta_optimo = np.dot((np.dot(inv_Xe_t_X, Xe_t)), Y)
breakpoint()
y_estimado = X_entrenamiento.dot(beta_optimo)
print(Y)
Y_estimado = np.matrix(y_estimado)

print(sum((Y-y_estimado)**2))
ECM = (1/len(X_entrenamiento)) * (sum((Y-y_estimado))**2)
# print(ECM)