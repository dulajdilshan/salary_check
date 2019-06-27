import socket
import threading
from enum import Enum

from libx import user1 as bob
from user_functions import *


# bob.InitOT(1)  # for client

class ApplicationType(Enum):
    SERVER = 0
    CLIENT = 1


class ApplicationStatus(Enum):
    WAITING = 0
    RUNNING = 1
    STOPPED = 2


def send_x(connection):
    while True:
        x = input("x: ")
        y = input("y: ")
        xy = x + '$' + y
        print(xy)
        connection.send(bytes(xy, 'utf-8'))


applicationType = ApplicationType.CLIENT

peer = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Try to start as a client. If failed, then start as a server and wait a client
try:
    sock.connect((peer, 10000))
except ConnectionRefusedError:
    sock.bind(('0.0.0.0', 10000))  # binding to local network card, port 10000
    sock.listen(1)
    applicationType = ApplicationType.SERVER

# Set up user
bob.InitOT(applicationType.value)

# Different implementations for Client and Server
if applicationType == ApplicationType.SERVER:
    securityParam = generate_security_params(bob)
    conn, addr = sock.accept()
    sock = conn
    pass
else:
    pass

valuesReceivedStatus = {'blindedK': False, 'otherP': False, 'otherQ': False, 'blindedR': False, 'otherA': False,
                        'otherE': False}

receivedValues = {'blindedK': '', 'otherP': '', 'otherQ': '', 'blindedR': '', 'otherA': '',
                  'otherE': ''}

# Generate Blinded Key
bobBKey = bob.GetBlinedKey()

# pass -> to Alice and get from alice

# get salary
bobSalary = 503554646651
bob.SetCompareValue(bobSalary)

print("Bob: Connected to Alice")

key = "first key"
value = "first value"

# Protocol
with sock:
    iThread = threading.Thread(target=send_x, args=(sock,))
    iThread.daemon = True
    iThread.start()

    running = True

    while running:
        running = False
        if value != 0:
            data = sock.recv(1024)
            key, value = extractData(str(data, 'utf-8'))
            print(key, value)
        else:
            print(ApplicationStatus.STOPPED)
            break

        for received in valuesReceivedStatus.values():  # Listen receiving port till all the values arrive
            if not received:
                running = True

        if not running:
            # Do the final calculation and return the value
            # ans = functionX()
            # print("Salaries: ", ans)
            pass
