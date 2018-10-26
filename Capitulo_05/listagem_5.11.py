'''Soma de 5 números'''

n = 1       #O contador inicial começa em 1 e vai até 5
soma = 0

while n <= 5:
    x = int(input('Digite o {} número: '.format(n)))
    soma = soma + x   #Aqui é o acumulador pra fazer a soma
    n = n + 1   #Aqui o contador pra ir incrementando de 1 em 1
print('Soma: {}'.format(soma))
