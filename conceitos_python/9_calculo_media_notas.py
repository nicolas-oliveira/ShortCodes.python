# Cálculo da média de um conjunto de notas em Python

qtd_notas = 5
nota, soma, media = 0, 0, 0

for _ in range(1, qtd_notas + 1):
    nota = float(input("NOTA: "))
    soma += nota

media = soma / qtd_notas
print("A média é: ", media)
