'''3.8 - Escreva um programa que leia um valor em metros
e o exiba convertido em milimetros'''

v_metros = float(input('Digite o valor em metros: '))

v_mm = v_metros * 1000

print('%.2fm é igual %.2fmm' %(v_metros, v_mm))