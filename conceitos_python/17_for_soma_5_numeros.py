# Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
# e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de
# repetição para somar todos os valores digitados

numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

soma = 0
for numero in numeros:
    soma += numero

print("A soma dos números é:", soma)
