# Iteração sobre as linhas de uma matriz utilizando a biblioteca NumPy em Python

import numpy as np

matriz = np.array([[1,2,3], [4,5,6]])

for i in range(matriz.shape[0]):
    print(matriz[i])
