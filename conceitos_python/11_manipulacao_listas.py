# Demonstração de manipulação de listas em Python
# Exemplo de lista
lista_exemplo = ['Gato', 'Cachorro', 'Gorila', 'Cavalo']
print("Lista original:", lista_exemplo)

print(lista_exemplo.index('Gato'))

# Modificando a lista (mutável)
lista_exemplo[2] = 'Pintinho'
print("Lista após modificação:", lista_exemplo)

# Adicionando um elemento à lista
lista_exemplo.append('Samambaia')
print("Lista após adição:", lista_exemplo)

# Removendo um elemento da lista
lista_exemplo.remove('Gato')
print("Lista após remoção:", lista_exemplo)

lista_exemplo.remove(lista_exemplo[0])
print("Lista após remoção:", lista_exemplo)

del lista_exemplo

# print(lista_exemplo)
