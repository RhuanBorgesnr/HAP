'''
Rhuan Borges - 2022

'''
from matplotlib import pyplot as plt
import numpy as np

# dados a serem gerados aleatoriamente
dados = np.random.rand(10, 1000)


# X e Y dos dados gerados
x = dados[:, 0].reshape(dados.shape[0], 1)
X = np.append(x, np.ones((dados.shape[0], 1)), axis=1)
y = dados[:, 1].reshape(dados.shape[0], 1)

# Calculando os parâmetros
calc = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)


# calculando os valores do eixo 
y_linha = X.dot(calc)

# Plotando os pontos de dados
plt.scatter(x, y)
plt.plot(x, y_linha, 'r')
plt.title('')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
