# Matriz: Dada a matriz abaixo, construa uma estrutura de repetição
# para percorrer e somar todos os elementos da matriz
import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
                   
# -----------------------------------------------------------                   
                   
                   
# Inicializando a variável para armazenar a soma dos elementos
soma = 0

# Percorrendo a matriz e somando os elementos
for linha in matriz:
    for elemento in linha:
        soma += elemento

# Exibindo a soma dos elementos da matriz
print("A soma de todos os elementos da matriz é:", soma)
