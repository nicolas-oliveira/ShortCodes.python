tempo = float(input("TEMPO (horas): "))
velocidade_media = float(input("VELOCIDADE MEDIA (km/h): "))

DISTANCIA = tempo * velocidade_media
LITROS_USADOS = DISTANCIA / 12

print(
    f'\n\nTempo: {tempo} horas\n'
    f'Velocidade: {velocidade_media} km/h\n'
    f'Distância: {DISTANCIA} km\n'
    f'Litros: {round(LITROS_USADOS, 1)} litros'
)