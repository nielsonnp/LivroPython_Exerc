'''Cálculo de média com acumulador'''

x = 1
soma = 0

while x <= 5:
    n = float(input('Digite a {} nota: '.format(x)))
    soma = soma + n
    x = x + 1
print('Média: {}'.format(soma/5))