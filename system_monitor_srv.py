import psutil
import socket
import time

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print ("Cliente conectado",cliente)
        time.sleep(3)
        send_msg = 'cpu percent: '+str(psutil.cpu_percent())+'\
            - memory usage percent: '+ str(psutil.virtual_memory().percent)
        con.send(send_msg.encode())
    print ('Finalizando conexao do cliente', cliente)
    con.close()