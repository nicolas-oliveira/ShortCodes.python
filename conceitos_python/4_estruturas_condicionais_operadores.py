# Uso de estruturas condicionais if-else com operadores matemáticos em Python
n1 = float(input("DIGITE A NOTA 1: "))
n2 = float(input("DIGITE A NOTA 2: "))
n3 = float(input("DIGITE A NOTA 3: "))

media = (n1 + n2 + n3) / 3
if (media >= 0.0) and (media <= 4.0):
    print(f'\n\nNOTA: {round(media, 1)}\nREPROVADO')
else:
    if (media >= 4.1) and (media < 6.0):
        print(f'\n\nNOTA: {round(media, 1)}\nPEGOU EXAME')
        exame = float(input("DIGITE A NOTA DO EXAME: "))
        if exame >= 6.0:
            print("APROVADO")
        else:
            print("REPROVADO")
    else:
        if media >= 6.0:
            print(f'\n\nNOTA: {round(media, 1)}\nAPROVADO')
