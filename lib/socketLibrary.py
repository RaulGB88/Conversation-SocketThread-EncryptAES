""" ---- SOCKET LIBRARY METHODS ---- """
def messagesText(socket, message):
    """ SEND plane TEXT and RECIEVE plane TEXT """

    # Send message
    socket.sendall(message.encode())

    # Recieve message
    data = socket.recv(1024)
    messageSend = data.decode()

    return messageSend

def messagesBinary(socket, message):
    """ SEND BINARY and RECIEVE BINARY """

    # Send message
    socket.sendall(message)

    # Recieve message
    data = socket.recv(1024)
    messageSend = data

    return messageSend
    
def messageSendBinary(socket, message):
    """ SEND BINARY and RECIEVE plane TEXT """

    # Send message
    socket.sendall(message)

    # Recieve message
    data = socket.recv(1024)
    messageSend = data.decode()

    return messageSend

def messageRecieveBinary(socket, message):
    """ SEND plane TEXT and RECIEVE BINARY """

    # Send message
    socket.sendall(message.encode())

    # Recieve message
    data = socket.recv(1024)
    messageSend = data

    return messageSend