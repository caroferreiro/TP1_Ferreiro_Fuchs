import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/Ejercicio_1/real-estate-valuation-data-set.csv')

datos_entrenamiento = df.iloc[0:317]
datos_test = df.iloc[317:]

#queremos estimar el precio por ping

x1 = list(datos_entrenamiento["X1 transaction date"].values)
X1 = np.array([[x1[i]] for i in range(0, len(x1))])
x2 = list(datos_entrenamiento["X2 house age"].values)
X2 = np.array([[x2[i]] for i in range(0,len(x2))])
x3 = list(datos_entrenamiento["X3 distance to the nearest MRT station"].values)
X3 = np.array([[x3[i]] for i in range(0,len(x3))])
x4 = list(datos_entrenamiento["X4 number of convenience stores"].values)
X4 = np.array([[x4[i]] for i in range(0,len(x4))])
x5 = list(datos_entrenamiento["X5 latitude"].values)
X5 = np.array([[x5[i]] for i in range(0,len(x5))])
x6 = list(datos_entrenamiento["X6 longitude"].values)
X6 = np.array([[x6[i]] for i in range(0,len(x6))])
y = list(datos_entrenamiento["Y house price of unit area"].values)
Y = np.array([[y[i]] for i in range(0,len(y))])




beta1 = 0
beta2 = 0
beta3 = 0
beta4 = 0
beta5 = 0
beta6 = 0

