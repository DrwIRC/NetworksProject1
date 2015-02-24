import os
from socket import *

#serverName = raw_input('Name of Host to Connect to: ')
serverName = ""
serverPort = 80
a = []
checker = None
cached = None

def sendgetrequest(path, serverName):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    request = 'GET ' + path + ' HTTP/1.1\r\n' \
            'Host: ' + serverName + '\r\n' \
            'Connection: close\r\n' \
            'Cache-Control: max-age=0' \
            'User-Agent: Lafayettescape/1.0\r\n' \
            'Accept-Charset: UTF-8\r\n' \
            '\r\n'
    clientSocket.send(request)
    modifiedSentence = clientSocket.recv(2048)
    print (modifiedSentence)
    text_file = open(path.replace("/",""), "w")
    text_file.write(modifiedSentence)
    text_file.close()
    clientSocket.close()

def sendheadrequst(path, serverName):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    request = 'HEAD ' + path + ' HTTP/1.1\r\n' \
            'Host: ' + serverName + '\r\n' \
            'Connection: close\r\n' \
            'Cache-Control: max-age=0' \
            'User-Agent: Lafayettescape/1.0\r\n' \
            'Accept-Charset: UTF-8\r\n' \
            '\r\n'
    clientSocket.send(request)
    modifiedSentence = clientSocket.recv(2048)
    linestring = open(path.replace("/",""), 'r').read()
    c = linestring.split()
    b = modifiedSentence.split()
    if b[13:19] == c[13:19]:
        print linestring
    else:
        sendgetrequest(path, serverName)
    
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return 1
        
def main():
    serverName = raw_input('Name of Host to Connect to: ')
##  serverName = "www.cs.lafayette.edu"
    curdir = os.getcwd()
    counter = 0
    maxcount = 0
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
            a.append(path)

        if checker:
##          #path = "/~sadovnia/courses/s15/cs305/labs/index1.html"
            cached = find( path.replace("/","") ,curdir)
            #print cached
            if cached == 1:
                sendheadrequst(path, serverName)
            else:
                sendgetrequest(path, serverName)
    

main()
