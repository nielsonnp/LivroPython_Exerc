'''3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distancia a percorrer e a velocidade media esperada para a viagem.'''

d_perc = float(input('Distancia a percorrer: '))
v_media = float(input('Velocidade média esperada: '))

tempo = (d_perc / v_media)

print('Tempo é igual %.2f ' % tempo)