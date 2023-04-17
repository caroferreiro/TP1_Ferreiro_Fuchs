import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv('Parte3/real-estate-valuation-data-set.csv')

datos_test = datos.iloc[315:]

x = datos[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y = datos["Y house price of unit area"].astype(float)
X = np.array(x)

X_test = datos_test[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y_test = datos_test["Y house price of unit area"].astype(float)

# Trasponemos X:
Xt = np.transpose(X)

# Multiplicamos Xt por X:
Xt_X = np.dot(Xt, X)

# Invertimos la multiplicación anterior:
inv_Xt_X = np.linalg.inv(Xt_X)

# Calculamos el beta óptimo:
beta_optimo = np.dot((np.dot(inv_Xt_X, Xt)), Y)

y_estimado = X_test.dot(beta_optimo.T)
Y_estimado = np.array(y_estimado)


ECM = sum((Y_test-y_estimado)**2)/len(X_test)
print(ECM)