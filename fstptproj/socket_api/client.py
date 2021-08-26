import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'{"login": "hiphop.movengroove", "password": "7e2525314c25"}')
    #s.sendall(b'1b193a8bd680acb930634b0a26a41edb1960162ff613727ae87795b1befaebfe')
    data = s.recv(1024)

print('Received', repr(data))
