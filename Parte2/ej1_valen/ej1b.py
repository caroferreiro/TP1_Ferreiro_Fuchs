import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ejercicio_1.csv')
x = df['X'].to_numpy()
y = df['Y'].to_numpy()

print(np.dot(np.transpose(x), y))
#print(np.dot(x, x))
