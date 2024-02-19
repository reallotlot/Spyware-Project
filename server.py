#THIS SCRIPT WILL HANDLE THE SERVER
#IT WILL WORK ON CONNECTING THE GUI TO ALL THE PARTS OF THE PROJECT
#THIS WILL INCLUDE CONNECTING THE GUI (CLIENT) TO THE
#DATABASE AND THE ACTUAL DETECTION PROCESS, HOWEVER
#THE CLIENT WILL NOT ACTUALLY CONTROL ANYTHING AND WILL JUST TALK WITH
#THIS SCRIPT WHICH WILL RUN EVERYTHING BEHIND THE SCENES 
#RETURNING JUST THE RESULTS

#outside imports
import socket


#local imports
from Spyware_Manager import detection


#set up server settings
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555

ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)

sock.listen(0)

(client, addr) = sock.accept()
print(f"Connection established with {client} at {addr}")
msg = None
while True:
    while msg is None:
        msg = client.recv(2048).decode()
    if msg.lower() == "scan":
        res = detection.ScanFile()
        text = ",".join(str(i) for i in res if i != [])
        client.send(text.encode())
        
    msg = None