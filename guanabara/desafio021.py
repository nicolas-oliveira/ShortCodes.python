# Desafio 023
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

from pygame import mixer
mixer.music.load('/home/nicolas/Downloads/Hurricane.mp3', 'r')
mixer.music.play()