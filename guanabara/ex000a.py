#Identificar os tipos primitivos de forma horizontal
#Com desenho e .format
m = input('Digite algo:')
a = m.isnumeric()
b = m.isalpha()
c = m.istitle()
d = m.islower()
e = m.isupper()
f = m.isalnum()
print('====================================================================================')
print('= O valor é__Numérico__Alfanumérico__Capitalizada__Maiúsculo__Minúsculo___Spring  =')
print('= _________   {}    |    {}   |    {}    |    {}   |    {}  |  {}  ='.format(a, b, c, e, d, f))
print('====================================================================================')
