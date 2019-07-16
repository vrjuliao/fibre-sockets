import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
dest = ('127.0.0.1', 5000)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    msg = msg.decode('utf-8')
    print(cliente, msg)
    #udp.sendto (msg.upper().encode(), dest)
    udp.sendto (msg.upper().encode(), cliente)
 
udp.close()
