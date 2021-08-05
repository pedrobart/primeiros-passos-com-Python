import socket

ip = socket.gethostbyname(socket.gethostname()) # O meu IP
for port in range(65535): #Portas de 0-65535
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Protocolo TCP
        serv.bind((ip,port)) #vincular

    except:
        print("[Aberta] Porta Aberta: ",port)
    serv.close()
