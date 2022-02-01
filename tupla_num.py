"""
     -> gerar 5 numeros aleatorios 
     -> insere numa tupla
     -> Listagem de numeros gerados  
     -> Menor e Maior valor dos numeros da tupla
     
"""

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print("os valores são: ", end="")

for i in numeros:
    print(f'{i} ', end='')
    
print(f"\no maior valor é: {max(numeros)}, e o menor é: {min(numeros)}")


