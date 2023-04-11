import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ejercicio_2.csv')
x = list(df['X'].values)
y = list(df['Y'].values) 


plt.plot(x,y,'.', color = 'hotpink')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()