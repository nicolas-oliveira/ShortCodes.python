# Iteração sobre os caracteres de uma palavra e verificação da presença de uma letra em Python

palavra = input("DIGITE:")
letra_escolhida = input("DIGITE: ")

for letra in palavra:
    if letra == letra_escolhida:
        print("A letra escolhida está na palavra digitada")
