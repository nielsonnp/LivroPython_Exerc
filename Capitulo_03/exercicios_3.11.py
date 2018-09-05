'''3.11 - Faça um programa que solicite o preço de
uma mercadoria e o percentual de desconto. Exiba o valor
do desconto e o preço a pagar'''

produto = float(input('Digite o valor do produto: '))
p_desc = int(input('Digite o percentual de desconto: '))

valor_desc = (produto * p_desc) / 100

total_pagar = (produto - valor_desc)

print('Total a pagar com desconto R$%.2f' % (total_pagar))