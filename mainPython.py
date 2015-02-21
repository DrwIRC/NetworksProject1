from socket import *

serverName = input('Name of Host to Connect to: ')
serverPort = 12000

#Creates the client socket 
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)

#TCP Connection
clientSocket.connect(serverName, serverPort)


#What Object would you like 
objectName = input('What Object do you want to download?: ')


#Send a  Sentence (GET?)
sentence = input('Input Sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
cleitnSocket.close()
