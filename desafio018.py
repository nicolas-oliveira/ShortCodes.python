# Desafio 018# Faça um programa que leia um ângulo qualquer e mostre na tela o valor da seno, cosseno e tangente desse ângulofrom math import sin, cos, tan, radiansa = float(input('Digite o valor do ângulo em graus centígrados: '))print('O cosseno é: {:.2f} \nO seno é: {:.2f} \nA tangente é: {:.2f}'.format(cos(radians(a)), sin(radians(a)),                                                                          tan(radians(a))))