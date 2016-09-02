from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while 1:
    print "Ready to serve"
    connectSocket, addr = serverSocket.accept()
    try:
        message = connectSocket.recv(2048)
        print message
        request = message.splitlines()[0].split()
        method = request[0]
        if method == 'GET':
             filename = request[1]
             f = open(filename[1:])
             outputData = f.read()
             connectSocket.send(request[2]+' 200 OK\r\n\r\n')
             connectSocket.send(outputData)
        else:
            print 'unknow method: ' + method
        connectSocket.close();
    except IOError:
        connectSocket.send(request[2]+' 404 Not Found\r\n\r\n')
        connectSocket.close()
serverSocket.close()
