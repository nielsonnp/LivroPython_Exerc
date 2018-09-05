'''3.13 - Escreva um programa que converta uma temperatura
digitada em °C em °F . '''

g_cel = float(input('Digite a temperatura em °C: '))

f = ((9*g_cel)/5) + 32

print('%.2f °C convertido para Fahrenheit é igual a %.2f °F' %(g_cel, f))

'''Regra de °C pra °F
 f = ( (9 * g_cel) / 5 ) + 32'''

'''Regra de °F pra °C 
 C = (5  *  (F-32)  /  9)'''