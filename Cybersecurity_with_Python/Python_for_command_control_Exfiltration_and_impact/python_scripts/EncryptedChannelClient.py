import socket, os
from Crypto.Cipher import AES

host = "127.0.0.1"
port = 1337

key = b'Sixteen byte key'

def encrypt(data, key, iv):
    #pad data as needed
    data += " "*(16 - len(data) % 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

message = "Hello"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    iv = os.urandom(16)
    s.send(iv)
    s.send(bytes([len(message)]))
    encrypted = encrypt(message, key, iv)
    print(f"Sending {encrypted.hex()}")
    s.sendall(encrypted)