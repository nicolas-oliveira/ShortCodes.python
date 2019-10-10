#Primeira forma que criei de identificar tipos primitivos
#Totalmente vertical ou seja todas as linhas aparecem
n = input('Digite algo:')
print('O tipo primitivo é ', type(n))
print(n, 'é alfabético?', n.isalpha())
print(n, 'é numérico?', n.isnumeric())
print(n, 'é alfanumérico?', n.isalnum())
print(n, 'é decimal?', n.isdecimal())
print(n, 'tem espaços?', n.isspace())
print(n, 'é maiusculas?', n.isupper())
print(n, 'é minusculas', n.islower())
print(n, 'está capitalizada(maisculas e minusculas)', n.istitle())
