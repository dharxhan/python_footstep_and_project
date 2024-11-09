from socket import *
import threading
HOSTNAME="172.20.10.2"
PORT=5000
def startServer():
    sSocket = socket(AF_INET,SOCK_STREAM)
    sSocket.bind((HOSTNAME,PORT))
    sSocket.listen(5)
    print("Server started on:",HOSTNAME,"with:",PORT)
    while True:
        rClient, addr=sSocket.accept()
        print("client addr:",addr)
startServer()
