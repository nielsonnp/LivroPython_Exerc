'''O usuário digita o ínicio e o fim da tabuada'''

inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))

while inicio <= 10:
    print('{} x {} = {}'.format(fim, inicio, fim*inicio))
    inicio = inicio + 1