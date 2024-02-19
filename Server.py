import socket

#set up server settings
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555

ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)

sock.listen(0)

(client, addr) = sock.accept()
print(f"Connection established with {client} at {addr}")
client.send(b"Hello")
