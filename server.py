from socket import *
import os
import colorama
from colorama import Fore
colorama.init()

client=socket(AF_INET,SOCK_STREAM)
client.bind(("127.0.0.1",1234))
client.listen(1)
server,address=client.accept()


while True:
    terminal=server.recv(1234).decode()
    terminal=terminal+">"
    dastoor=input(Fore.GREEN+terminal)
    if dastoor == "cls":
        os.system("cls")
    if dastoor == "" or dastoor == '\n':
        
        client.send(b"EMPTY!")
        continue
        
    server.send(dastoor.encode())
    response=server.recv(1234).decode()
    print(response)



    