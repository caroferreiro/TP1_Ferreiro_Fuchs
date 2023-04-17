import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/real-estate-valuation-data-set.csv')

datos_entrenamiento = df.iloc[0:315]
datos_test = df.iloc[315:]

X_entrenamiento = datos_entrenamiento[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y_entrenamiento = datos_entrenamiento[["Y house price of unit area"]]

X_test = datos_test[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
Y_test = datos_test[["Y house price of unit area"]]

beta_entrenamiento = ((np.linalg.inv(np.transpose(X_entrenamiento).dot(X_entrenamiento))).dot(np.transpose(X_entrenamiento))).dot(Y_entrenamiento)


# y_estimado = X1.dot(beta1) + X2.dot(beta2) + X3.dot(beta3) + X4.dot(beta4) + X5.dot(beta5) + X6.dot(beta6)
y_estimado = X1_t.dot(beta1) + X2_t.dot(beta2) + X3_t.dot(beta3) + X4_t.dot(beta4) + X5_t.dot(beta5) + X6_t.dot(beta6)
print(y_test, y_estimado)
sum = 0
for i in range(0,len(y_test)):
    
    sum = sum + (y_test[i]-y_estimado[i])**2 

ECM = sum / len(y_test)

# sum1=0
# for i in range(0,len(y_test)):
#     sum1 = sum1 + (y_test[i]-y_estimado_v2[i])**2 

# ECM2 = sum1 / len(y_test)
print(ECM)


