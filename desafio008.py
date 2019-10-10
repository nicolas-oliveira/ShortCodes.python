# Desafio 008
# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

a = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde à: \n{} km \n{} hm \n{} dam \n{:.0f} cm \n{:.0f} dc \n{:.0f} mm'
      .format(a, (a/1000), (a/100), (a/10), (a*100), (a*10), (a*1000)))
