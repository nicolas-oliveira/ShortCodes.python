#Desafio 011
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

a = float(input('Qual o preço do produto em R$? '))
b = a * 0.95
print('O preço do produto teve desconto de R${} para R${:.2f}'.format(a, b))