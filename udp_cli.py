import socket
import time
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
orig = ('', 5000)
udp.bind(orig)
print('Para sair use CTRL+X\n')
send_msg = input()
received_msg = None
while send_msg != '\x18':
    udp.sendto (send_msg.encode(), dest)
    time.sleep(0.5)
    received_msg, cliente = udp.recvfrom(1024)
    print('===Mensagem uppercase: ', received_msg.decode('utf-8'))
    send_msg = input()

udp.close()
