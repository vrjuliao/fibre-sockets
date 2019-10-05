import socket
import sys
HOST = sys.argv[1] #IP do servidor obtido por arugmento de execucao
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
while True:
    tcp.send (' '.encode())
    modifiedSentence = tcp.recv(1024)
    print(modifiedSentence.decode('utf-8'))
tcp.close()