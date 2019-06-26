def generate_security_params(alice):
    # get the security parameter
    securityParam = alice.GetSecurityParam()

    # Get the security params from initiator(Alice)
    p = alice.GetPublicParams(0)
    g0 = alice.GetPublicParams(1)
    g1 = alice.GetPublicParams(2)
    g2 = alice.GetPublicParams(3)
    return p, g0, g1, g2


def sendInput(connection):
    '''
    send message extract from the inputs of the user.
    sendMsg() function encodes the user input to utf-8 and convert it to a bytestream and send over the network
    :param connection: c
    :return: None
    '''
    connection.send(bytes(input(""), 'utf-8'))


def receiveMsg(sock):
    '''
    Receive Message from the outside. Msg is send through the connection
    :param sock: socket of the application
    :return: 0 or data
    '''
    data = sock.recv(1024)
    return data


def handleReceiveMsg(sock):
    while True:
        data = sock.recv(1024)
        # print(str(data, 'utf-8'))
        print(str(data))


def handleSendMsg(conn):
    while True:
        # conn.send(bytes(input(""), 'utf-8'))
        conn.send(input(""))


def extractData(msg):
    if len(msg) > 1:
        r = msg.index('$')
        key = str(msg[:r])
        value = str(msg[r + 1:])
        return key, value
    return 0, 0

