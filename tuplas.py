#variaveis compostas = tuplas + listas + dicionarios

# () - lista 
# [] - tupla
# {} - dicionario

# tupla - variavel que armazena varios dados/elementos
# as tuplas são _imutáveis_

# lanche = ["hamburguer","sumo","pudim"]
#              0          1       2   -> elementos


#lanche = ["hamburguer","sumo","pizza","pudim"]

"""
print(lanche[1:])
print(lanche[-1])

"""

"""
print(len(lanche))

"""


# Programa com tupla totalmente preenchida com contagem por extenso. de ZERO até VINTE
# O programa deverá ler um numero pelo teclado/input entre 0 e 20, e mostrá-lo por extenso.

'''
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
         'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 
         'dezanove', 'vinte')

while True:
    numero = int(input("Digita um numero entre 0 e 20: "))
    if 0 <= numero <= 20:
        break
    else:
        print("tenta de novo...")
print(f"Escolheste o número {tupla[numero]}")    
    
'''




# crie uma tupla com os 20 primeiros colocados da tabela do campeonato de futebol, na ordem de colocação.

# A) Os 5 primeiros
# B) Os últimos 4 colocados
# C) Equipas em ordem alfabética
# D) Em que posição está o FCPorto

equipas = ('porto', 'sporting', 'benfica', 'braga', 'estoril', 
           'portimonense', 'vitoria', 'gil vicente', 'boavista', 
           'maritimo', 'arouca', 'P.ferreira', 'vizela', 'santa clara', 
           'tondela', 'famalicao', 'moreirense','B-SAD', 'PeRapados', 'Zes')

'''
#print(f'Lista de equipas: {equipas}')
print("####" * 15)
for t in equipas:
    print(t)
print("####" * 15)
print(f'Os primeiros 5 colocados são: {equipas[0:5]}')
print("-=-=" * 15)
print(f'Os Últimos 4 colocados são: {equipas[-4:]}')
print("-=-=" * 15)
print(f'Equipas em ordem alfabetica: {sorted(equipas)}')
print("-=-=" * 15)
print(f'FCPorto está na: {equipas.index("porto")+1}ª posição')

'''