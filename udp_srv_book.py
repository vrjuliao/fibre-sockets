from socket import *

SERVER_IP = ''
SERVER_PORT = 12000
ORIGIN = (SERVER_IP, SERVER_PORT)

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(ORIGIN)
print('Servidor em execucao')
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	message = message.decode('utf-8')
	print(clientAddress, message)
	modifiedMessage = message.upper() + ' - OK'
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)