from socket import *
import sys

if len(sys.argv) != 4:
    print "command format: hostname hostport filename"

serverName =sys. argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('GET '+'/'+filename+' HTTP/1.1\r\n'+'HOST: '+serverName+'\r\n')
message = clientSocket.recv(2048)
print message

clientSocket.close()

