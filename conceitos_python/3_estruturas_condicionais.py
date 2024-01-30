# Uso de estruturas condicionais if-else em Python

idade = int(input("IDADE:"))

if idade < 0:
    print("MENSAGEM INVÁLIDA")

if (idade >= 0) and (idade <= 12):
    print("CRIANÇA")
else:
    if (idade >= 13) and (idade <= 17):
        print("ADOLESCENTE")
    else:
        if idade >= 18:
            print("ADULTO")

