'''3.14 - Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuario, assim como a quantidade de dias pelos quais o carro foi alugado.
calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado'''

km_perc = float(input('Quantos km foi percorrido? '))
dias = float(input('Quantos dias ficou com o carro alugado? '))

custo_km = (km_perc * 0.15)

custo_dia = (dias * 60)

total_pagar = (custo_km + custo_dia)

print('Valor a pagar:\n'
      'R$%.2f por km rodado e R$%.2f por dia\n'
      'Total = R$%.2f' % (custo_km, custo_dia, total_pagar))