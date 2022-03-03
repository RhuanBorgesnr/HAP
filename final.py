'''
Rhuan Borges - 2022

'''

'''
Rhuan Borges - 2022

'''

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure
import matplotlib.pyplot as plt
from numpy.random import rand


 
m = rand(3,3) # é uma matriz de (x,y,z) de coordenadas
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(m)): #plota cada ponto + seu índice 
  x = m[i,0]
  y = m[i,1]
  z = m[i,2]
  label = i
  ax.scatter(x, y, z, color='b')
#   plt.plot(x, y) 
  ax.text(x, y, z, '%s' % (label), size=20, zorder=1, color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pyplot.show()
