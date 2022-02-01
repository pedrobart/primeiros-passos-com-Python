'''
 Escreva um programa que leia um valor em metros 
 e o exiba convertido em milímetros,
 aceitar virgulas na entrada do usuário:
 
'''

# Milímetro (mm)
# → O milímetro equivale a dividir o metro em 1000 partes iguais, ou seja,
# 1 metro : 1000 = 1 mm.

'''
Operador	                       
+ (Adição ou sinal positivo)	        
- (Subtração ou sinal negativo)	       
* (Multiplicação)	                   
/ (Divisão)	                           
// (Divisão inteira)	               
% (Módulo)	                           
** (Exponenciação)	                    
'''

print('____Conversor de Metros para Milimetros___')

metros = int(input(f'Digite o Numero de Metros para ser convertido: '))

milímetros = metros*1000

print(f'O resultado é: {milímetros}mm')
