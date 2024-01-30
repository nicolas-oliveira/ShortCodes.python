#Forma completa de identificar alguns tipos primitivos e seus derivados
#Vertical mas com apenas as linhas verdadeiras
a = input('Digite algo: ')

if a.isnumeric() == True:
    print('é um número')
if a.isalpha() == True:
    print('é alfa numérico')
if a.isspace() == True:
    print('é apenas um espaço')
if a.islower() == True:
    print('só sei que é tudo minúsculo')
if a.istitle() == True:
    print('só sei que está entitulado')
if a.isupper() == True:
    print('está tudo maiúsculo')
if a.isidentifier() == True:
    print('isso é identifier')
if a.isdigit() == True:
    print('isso é um dígito')

