# Demonstração de manipulação de dicionários em Python

# Dicionarios
contagem = {"Adultos": 22, "Crianças": 12, "Idosos": 30}
print(contagem)
print([key for key, value in contagem.items() if value == 22][0])

contagem["Alienígenas"] = 0

print(contagem.items())
print(contagem.values())
print(contagem.keys())
print()

del contagem["Alienígenas"]
print(contagem)
print()

nova_contagem = {"Adultos": 102, "Alienígenas": 10}
contagem.update(nova_contagem)
print(contagem)
print()

for faixa_etaria, qtd_faixa_etaria in contagem.items():
    print(
        f"Faixa etária: {faixa_etaria}\nQuantidade de pessoas: {qtd_faixa_etaria}\n\n"
    )
