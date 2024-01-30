#Desafio 011
#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2m²

a = float(input('Em metros qual a largura da parede? '))
b = float(input('Em metros qual a altura da parede? '))
area = a * b
tinta = area / 2
print('A área da parede é {:.2f}m² e a quantidade de tinta necessária é {:.2f} litros'.format(area, tinta))
print('Sabendo que cada litro é usado em 2m²')