import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/real-estate-valuation-data-set.csv')

datos_entrenamiento = df.iloc[0:315]
datos_test = df.iloc[315:]


# x1 = list(datos_entrenamiento["X1 transaction date"].values)
# X1 = np.array([[x1[i]] for i in range(0,len(x1))])
# x2 = list(datos_entrenamiento["X2 house age"].values)
# X2 = np.array([[x2[i]] for i in range(0,len(x2))])
# x3 = list(datos_entrenamiento["X3 distance to the nearest MRT station"].values)
# X3 = np.array([[x3[i]] for i in range(0,len(x3))])
# x4 = list(datos_entrenamiento["X4 number of convenience stores"].values)
# X4 = np.array([[x4[i]] for i in range(0,len(x4))])
# x5 = list(datos_entrenamiento["X5 latitude"].values)
# X5 = np.array([[x5[i]] for i in range(0,len(x5))])
# x6 = list(datos_entrenamiento["X6 longitude"].values)
# X6 = np.array([[x6[i]] for i in range(0,len(x6))])
# y = list(datos_entrenamiento["Y house price of unit area"].values)
# Y = np.array([[y[i]] for i in range(0,len(y))])

X_entrenamiento = datos_entrenamiento[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y_entrenamiento = datos_entrenamiento[["Y house price of unit area"]]

beta_entrenamiento = ((np.linalg.inv(np.transpose(X_entrenamiento).dot(X_entrenamiento))).dot(np.transpose(X_entrenamiento))).dot(Y_entrenamiento)
#beta0 = ((np.linalg.inv(np.transpose(X0).dot(X0))).dot(np.transpose(X0))).dot(Y)
# beta1 = ((np.linalg.inv(np.transpose(X1).dot(X1))).dot(np.transpose(X1))).dot(Y)
# beta2 = ((np.linalg.inv(np.transpose(X2).dot(X2))).dot(np.transpose(X2))).dot(Y)
# beta3 = ((np.linalg.inv(np.transpose(X3).dot(X3))).dot(np.transpose(X3))).dot(Y)
# beta4 = ((np.linalg.inv(np.transpose(X4).dot(X4))).dot(np.transpose(X4))).dot(Y)
# beta5 = ((np.linalg.inv(np.transpose(X5).dot(X5))).dot(np.transpose(X5))).dot(Y)
# beta6 = ((np.linalg.inv(np.transpose(X6).dot(X6))).dot(np.transpose(X6))).dot(Y)


# y_estimado = [[x1[i]*beta1 + x2[i]*beta2 + x3[i]*beta3 + x4[i]*beta4 + x5[i]*beta5 + x6[i]*beta6]  for i in range(0,len(x1))]
# y_estimado = X1.dot(beta1) + X2.dot(beta2) + X3.dot(beta3) + X4.dot(beta4) + X5.dot(beta5) + X6.dot(beta6)
y_estimado = X_entrenamiento.dot(beta_entrenamiento)

sum = 0
for i in range(0,len(Y_entrenamiento)):
    sum = sum + (Y_entrenamiento[i]-y_estimado[i])**2

ECM = sum / len(Y_entrenamiento)
print(ECM)