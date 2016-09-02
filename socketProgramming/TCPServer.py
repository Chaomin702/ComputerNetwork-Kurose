from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while 1:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048)
#    modifyMessage = message.upper()
#    connectionSocket.send(modifyMessage)
    print message
    connectionSocket.close()
