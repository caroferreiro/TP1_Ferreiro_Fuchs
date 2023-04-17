import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/real-estate-valuation-data-set.csv')

datos_entrenamiento = df.iloc[0:315]
datos_test = df.iloc[315:]

X_entrenamiento = datos_entrenamiento[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y_entrenamiento = datos_entrenamiento[["Y house price of unit area"]]

beta_entrenamiento = ((np.linalg.inv(np.transpose(X_entrenamiento).dot(X_entrenamiento))).dot(np.transpose(X_entrenamiento))).dot(Y_entrenamiento)


print(beta_entrenamiento)