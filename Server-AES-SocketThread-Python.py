import base64
from encodings import utf_8
import os
import socket
import sys
import threading
from unicodedata import name
import lib.socketLibrary
import lib.encryptAES
import random

from Crypto.Cipher import AES


# Decidimos la IP y el puerto del servidor
HOST = '127.0.0.1'  # La IP del servidor es la loca de la máquina
PORT = 5008  # El puerto tiene que ser superior a 1024, por debajo estan reservados
finished_message = b''

NAME = b'Hola. Como te llamas? (Cuando quieras terminar esta conversacion indicamelo con un [bye]).'
BYE = 'bye'
CONTINUE = 'Si quieres terminar de jugar escribe: [bye] ...: '
MESSAGE_TO_INPUT = "Indica tu mensaje: "

def server_program():
    """ Ejecuta el programa Servidor """
    try:
        socket_escucha = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket servidor creado')
    except socket.error:
        print('Fallo en la creación del socket servidor')
        sys.exit()

    try:
        # Definimosel punto de enlace del ervidor. El servidor está preparado en la IP 127.0.0.1 y puerto 5000
        socket_escucha.bind((HOST, PORT))
    except socket.error as e:
        print('Error socket: %s' % e)
        sys.exit()
        
    # El servidor puede escuchar hasta 5 clientes. En este ejmeplo sólo escuchará a 1 y se rompe la conexión
    socket_escucha.listen(5)

    while True:
        # El Servidor queda bloquedo en esta línea esperando a que un cliente se conecte a su IP y puerto
        # Si un cliente se conecta guardamos en conn del socket y en addr la información del cliente (IP y puerto del cliente)
        socket_server, addr_cliente = socket_escucha.accept()

        # Ejecución con Threads.
        lock = threading.Lock()
        t = threading.Thread(target=execute, args=(lock,socket_server,addr_cliente))
        t.start()


def execute(lock, socket_server, addr_cliente):
    """ Ejecuta la logica del programa """

    with lock:
        with socket_server:

            close = False
            key = os.urandom(16)
            iv = os.urandom(AES.block_size)

            print(f'Conexión exitosa con el cliente. {addr_cliente}')

            # Send a Key to Client and get message to Client
            message = lib.socketLibrary.messageSendBinary(socket_server, key)
            # Send an IV to Client and get message to Client
            message = lib.socketLibrary.messagesBinary(socket_server, iv)

            """ Give the name of Client """
            # Encrypte the NAME messsage
            encrypted_message = lib.encryptAES.encrypte(NAME, key, iv)
            # Send the encrypted message with a key and recieve an encrypted message of Client
            recieve_encrypted_message = lib.socketLibrary.messagesBinary(socket_server, encrypted_message)
            # Decrypte the message of Client with a key
            recieve_decrypted_message = lib.encryptAES.decrypte(recieve_encrypted_message, key, iv)
            # Update a text to send a Client with his/her name
            client_name = "Hola " + recieve_decrypted_message.decode()
            

            """ Hi Client """
            # Encrypte the messsage to send a Client with his/her name
            encrypted_message = lib.encryptAES.encrypte(client_name.encode(), key, iv)
             # Send the encrypted message with a key and recieve an encrypted message of Client
            recieve_encrypted_message = lib.socketLibrary.messagesBinary(socket_server, encrypted_message)
            # Decrypte the message of Client with a key
            recieve_decrypted_message = lib.encryptAES.decrypte(recieve_encrypted_message, key, iv)
            recieve_decrypted_message = recieve_decrypted_message.decode("utf-8")
            # Print a decrypted message of Client
            print(recieve_decrypted_message)

            while not close:

                # Check if the Client want disabled
                if recieve_decrypted_message == finished_message or recieve_decrypted_message == BYE:
                    close = True
                    # Put BYE into the input_message value
                    input_message = BYE
                else:
                    # Input the message
                    input_message = input(MESSAGE_TO_INPUT)

                # Encrypte the input messsage
                encrypted_message = lib.encryptAES.encrypte(input_message.encode(), key, iv)
                # Send the encrypted message with a key and recieve an encrypted message of Client
                recieve_encrypted_message = lib.socketLibrary.messagesBinary(socket_server, encrypted_message)
                # Decrypte the message of Client with a key
                recieve_decrypted_message = lib.encryptAES.decrypte(recieve_encrypted_message, key, iv)
                recieve_decrypted_message = recieve_decrypted_message.decode("utf-8")
                # Print a decrypted message of Client
                print(recieve_decrypted_message)


if __name__ == '__main__':
    server_program()
