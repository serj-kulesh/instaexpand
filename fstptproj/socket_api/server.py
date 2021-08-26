import socket
from InstagramAPI import InstagramAPI
import json
import hashlib

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
api_objects = dict()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            logopass = json.loads(data)
            if 'login' in logopass:
                logopass_str = str(logopass['login']) + str(logopass['password'])
                hash = hashlib.sha256(logopass_str.encode()).hexdigest()
                i_api = InstagramAPI(logopass['login'], logopass['password'])
                api_objects[hash] = i_api.login()
                
                conn.sendall(hash.encode())
                
            if 'hash' in logopass:
                if logopass['hash'] in api_objects:
                    conn.sendall(b'found! Try commands')
                else:
                    conn.sendall(b'not found')
            #conn.sendall(b'no data recieved')
            
