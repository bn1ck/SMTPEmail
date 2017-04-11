from socket import *

def main():
    msg = '\r\n This is the content of the email address'
    endmsg = '\r\n.\r\n'
    mailServer = 'localhost'
    mailPort = 25
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailServer, mailPort))

    recv = clientSocket.recv(1024)
    print recv

    if recv[:3] != '220':
        print '220 reply not recieved from the server'

    helloCommand = 'Hello User\r\n'
    clientSocket.send(helloCommand)
    recv1 = clientSocket.recv(1024)
    print recv1

    if recv1[:3] != '250':
        print '250 reply not recieved from the server'

    clientSocket.send('Mail FROM: <bill@gates.com>\r\n')
    recv1 = clientSocket.recv(1024)
    print recv1

    if recv1[:3] != '250':
        print '250 reply not recieved from the server'

    clientSocket.send('RCPT TO: <balatsky@csus.edu> \r\n')
    recv1 = clientSocket.recv(1024)
    print recv1

    if recv1[:3] != '250':
        print '250 reply not recieved from the server'

    clientSocket.send('DATA \r\n')
    recv1 = clientSocket.recv(1024)
    print recv1

    if recv1[:3] != '354':
        print '354 reply not recieved from the server'

    clientSocket.send('\r\n')
    clientSocket.send(msg)
    clientSocket.send(endmsg)
    recv1 = clientSocket.recv(1024)
    print recv1

    if recv1[:3] != '250':
        print '250 reply not recieved from the server'

    clientSocket.send('QUIT\r\n')
    clientSocket.close()

    pass

if __name__ == '__main__':
    main()