import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ejercicio_1.csv')
x = list(df['X'].values)
y = list(df['Y'].values)

for i in range (len(y)):
    y[i] += 12


plt.plot(x,y,'.', color = 'royalblue')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()