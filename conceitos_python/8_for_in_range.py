# Utilização da função range() para gerar uma sequência de números inteiros 
# no intervalo [inicio, final] em Python.

num = 3
inicio = 1
final = 10

for n in range(inicio, final + 1):
    print(f"{num} x {n} = {num * n}")
