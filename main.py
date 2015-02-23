a = []
counter = 0
maxcount = 0
while True:
    n = raw_input("b f r q else:")

    if n == 'b':
        if counter > 0
            counter = counter - 1
            print "clientSocket.send(getword at counter)"
            print "you went back\n"
        else
            print "you cant back\n"

    elif n == 'f':
        if counter < maxcount
            counter = counter + 1
            print "clientSocket.send(getword at counter)"
            print "you went forward\n"
        else
            print "you cant forward\n"

    elif n == 'r':
        print "clientSocket.send(getword at counter)"
        print "refresh\n"

    elif n == 'q':
        print "quit\n"
        break

    else:
        maxcount = maxcount + 1
        a.append(n)
        print "clientSocket.send(n)"
