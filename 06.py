'''
 Escreva um código Python para implementar o algoritmo para imprimir o maior número entre dois números em Python
'''

num1 = int(input('digite o numero: '))
num2 = int(input('digite o segundo numero: '))
for i in range(num1+num2):
    if num1 > num2:
        print(f'O numero {num1} é maior.')
        break
    else:
        print(f'o Numero {num2} é maior')
        break
        