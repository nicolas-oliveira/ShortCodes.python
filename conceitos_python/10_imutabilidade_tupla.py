# Demonstração das propriedades de imutabilidade de uma tupla em Python
# IMUTÁVEL
tupla = ('a', 'b', 'c')

print(tupla[0])

print(tupla.index('b'))

# Tentando modificar a tupla (imutável - isso resultará em um erro)
# tupla[2] = 10  # Isso causará um TypeError
