import os
from socket import *

#serverName = raw_input('Name of Host to Connect to: ')
serverName = "www.cs.lafayette.edu"
serverPort = 80

a = []
counter = 0
maxcount = 0
checker = None
cached = None
while True:
    n = raw_input("b f r q else:")
    checker = True
    if n == 'b':
        if counter > 1:
            counter = counter - 1
            path = a[counter - 1]
            print "SUCCESS: YOU WENT BACK\n"
        else:
            checker = False
            print "ERROR: YOU CANNOT GO BACK\n"

    elif n == 'f':
        if counter < maxcount:
            counter = counter + 1
            path = a[counter - 1]
            print "SUCCESS: YOU WENT FORWARD\n"
        else:
            checker = False
            print "ERROR: YOU CANNOT GO FORWARD\n"

    elif n == 'r':
        if not a:
            print "ERROR: YOU CANNOT REFRESH"
            checker = False
        else:
            path = a[counter-1]
            print "SUCCESS: REFRESHED\n"

    elif n == 'q':
        print "YOU JUST QUIT\n"
        checker = False
        break

    else:
        path = n
        maxcount = maxcount + 1
        counter = maxcount
        a.append(n)

    if checker:
        #check to see if cached
        apple = os.getcwd()
        print apple
        if cached:
            #read and print out file
            banana = 0
        else:
            #path = "/~sadovnia/courses/s15/cs305/labs/index1.html"
            #Creates the client socket 
            clientSocket = socket(AF_INET, SOCK_STREAM)

            #TCP Connection
            clientSocket.connect((serverName, serverPort))
            request = 'GET ' + path +' HTTP/1.1\r\n' \
                    'Host: ' + serverName + '\r\n' \
                    'Connection: close\r\n' \
                    'Cache-Control: max-age=0' \
                    'User-Agent: Lafayettescape/1.0\r\n' \
                    'Accept-Charset: UTF-8\r\n' \
                    '\r\n'
            clientSocket.send(request)
            modifiedSentence = clientSocket.recv(2048)
            #save to a file
            print (modifiedSentence)
            clientSocket.close()

    
