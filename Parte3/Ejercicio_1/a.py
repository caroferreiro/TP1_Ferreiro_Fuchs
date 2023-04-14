import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/Ejercicio_1/real-estate-valuation-data-set.csv')

datos_entrenamiento = df.iloc[0:315]
datos_test = df.iloc[315:]


x1 = list(datos_entrenamiento["X1 transaction date"].values)
X1 = np.array([[x1[i]] for i in range(0,len(x1))])
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


#beta0 = ((np.linalg.inv(np.transpose(X0).dot(X0))).dot(np.transpose(X0))).dot(Y)
beta1 = ((np.linalg.inv(np.transpose(X1).dot(X1))).dot(np.transpose(X1))).dot(Y)
beta2 = ((np.linalg.inv(np.transpose(X2).dot(X2))).dot(np.transpose(X2))).dot(Y)
beta3 = ((np.linalg.inv(np.transpose(X3).dot(X3))).dot(np.transpose(X3))).dot(Y)
beta4 = ((np.linalg.inv(np.transpose(X4).dot(X4))).dot(np.transpose(X4))).dot(Y)
beta5 = ((np.linalg.inv(np.transpose(X5).dot(X5))).dot(np.transpose(X5))).dot(Y)
beta6 = ((np.linalg.inv(np.transpose(X6).dot(X6))).dot(np.transpose(X6))).dot(Y)


