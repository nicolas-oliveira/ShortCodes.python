# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

A = float(input('Quanto de grana você tem na carteira?R$ '))
B = A / 4.06
print('Com R${} você tem U${:.2f}'.format(A, B))
