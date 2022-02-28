'''
Rhuan Borges - 2022

'''
from math import sqrt

import math
import numpy as np
from matplotlib import pyplot as plt

# Gerar dados aleatorios 
x = np.array(range(10))*0.5
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])


# Criando grafico
plt.subplot(111)
plt.plot(x,y,marker='o')
plt.xlabel(" X")
plt.ylabel(" Y")
plt.title("")
plt.subplot(111)


plt.show()
