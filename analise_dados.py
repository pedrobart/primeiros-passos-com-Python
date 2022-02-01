'''
-> input com 5 valores e armazenado em tupla 
-> quantas vezes aparece o valor 9
-> Em que posição foi digitad o primeiro valor 3
-> Quais foram os numeros pares

'''

num_rep = 5

#ciclo for com 5 tentativas de input 


for i in range(num_rep):
    x = [int(input('digite 5 numeros: '))]
print(x)
          
    
# se o input exceder as 5 tentativas o ciclo for quebra    
if i == num_rep:
    raise ValueError

