#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print ("Incoming:", addr)
        try:
            message = connectionSocket.recv(1024)
            print(message)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            #Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode())
            connectionSocket.send('Content-Type: text/html\n\n'.encode())
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            connectionSocket.send('HTTP/1.0 404 Not Found\r\n'.encode())

            #Fill in end

            #Close client socket
            connectionSocket.close()


    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
