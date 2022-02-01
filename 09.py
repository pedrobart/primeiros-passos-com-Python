"""
calcular a area de um cilindro 
"""

h = int(input("altura do cilindro: "))

r = int(input('raio do cilindro: '))



pi = 3.14

total = 2 * pi * r * (r + h)



print(f'o volume do cilindro é: {total} metros quadrados')