import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dftest.csv', sep=';')

nbCases = df['NbCases']
nbDeaths = df['NbDeaths']
barrelPrice = df['BarrelPrice']
