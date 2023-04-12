import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Parte3/Ejercicio_1/real-estate-valuation-data-set.csv')

datos_entrenamiento = df.iloc[0:315]
datos_test = df.iloc[315:]



