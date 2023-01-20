import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('localhost', 8001))  
Op1 = 'Op1'
Op2 = 'Op2'
print(Op1)
sock.send(Op2)  
sock.close()