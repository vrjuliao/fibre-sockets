from socket import *
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12000
SERVER = (SERVER_IP, SERVER_PORT)
udp_client_socked = socket(AF_INET, SOCK_DGRAM)

print('Socket cliente em execucao\nPara sair use CTRL+X')
print('=== Digite caracteres minusculos: ')
send_msg = input()
received_msg = None
while send_msg != '\x18':
    udp_client_socked.sendto(send_msg.encode(), SERVER)
    time.sleep(0.5)
    received_msg, _ = udp_client_socked.recvfrom(2048)
    print('=== Resposta do servidor: \n', received_msg.decode('utf-8'), '\n')
    print('=== Digite caracteres minusculos: ')
    send_msg = input()

udp_client_socked.close()