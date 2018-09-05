'''3.10 - Faça um programa que calcule o aumento de um salário. Ele
deve solicitar o valor do salário e a porcentagem do aumento. Exiba
o valor do aumento e do novo salário'''

salario = float(input('Valor do salário: '))

aumento = int(input('Aumento de quantos porcento? '))

v_aumento = (salario * aumento) / 100

novo_salario = (salario + v_aumento)

print('Seu novo salario é de %.2f' %(novo_salario))