"""
Python e uma linguagem orientada a objetos, ou seja, praticamente tudo em python é um objeto, com propriedades de metodos.
e uma classe nada mais é do que o construtor daquele objeto, 
como se ofsse uma planta de uma casa ou de um projeto, são as instrucoes de como ele funciona e se deve comportar.
"""
    
    
    
class Carro:
    def __init__(self,marca,modelo,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ligar_carro = False
        self.velocidade = 0
        
        
    def ligar(self):
        if self.ligar_carro:
            print("Carro ligado, prossegue")
        else:
            self.ligar_carro = True
            print("Carro ligado")
            
            
    def desligar(self):
        if self.ligar_carro:
            self.ligar_carro = False
            print("Carro Desligado")
        else:
            print("Carro desligado, nada acontece")
    
    def acelerar(self):
        if self.ligar_carro:
            self.velocidade += 1
            print(f"{self.velocidade}km/h")
        else:
            print("não é possivel acelerar, carro desligado")
            
    def travao(self):
        if self.ligar_carro:
           self.velocidade -= 1
           print(f"{self.velocidade}km/h")
        else:
           print("não é possivel acelerar, o carro está desligado")