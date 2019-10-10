# Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

a = int(input('Digite um número: '))
b = a * 2
c = a * 3
d = pow(a, (1/2))
print('O dobro, triplo e raiz quadrada desse número é: {}, {} e {:.3f}'.format(b, c, d))
