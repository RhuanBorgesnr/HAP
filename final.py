'''
Rhuan Borges - 2022

'''

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure

 
m = rand(3,3) #m é uma matriz de (x,y,z) coordenadas
 
fig = figure()
ax = fig.add_subplot(projection='3d')

#plot cada ponto
for i in range(len(m)): 
    ax.scatter(m[i,0],m[i,1],m[i,2],color='b',cmap='cividis' ) 

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pyplot.show()
