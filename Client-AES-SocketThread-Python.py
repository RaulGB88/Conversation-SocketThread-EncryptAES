import imp
import socket
import sys
import lib.socketLibrary
import lib.encryptAES

from Crypto.Cipher import AES
from setuptools import sic

HOST = '127.0.0.1'
PORT = 5008

BYE = 'bye'
MESSAGE_TO_KEY = "Puedes mandarme la clave?"
MESSAGE_TO_IV = "Puedes mandarme el IV?"
MESSAGE_TO_INPUT = "Indica tu mensaje: "


def client_program():
    """ Ejecuta el programa Cliente """

    try:
        # 1- Creamos el Socket.
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket cliente creado')
    except socket.error:
        print('Fallo en la creación del socket cliente')
        sys.exit()

    # 2- Conectamos el Socket cliente al servidor
    socket_client.connect((HOST, PORT))

    execute(socket_client)


def execute(socket_client):
    """ Ejecuta la logica del programa """

    with socket_client:

        print(f'Conexión exitosa con el servidor.')

        key = socket_client.recv(1024)
        # Send message to Server to get a Key.
        #key = lib.socketLibrary.messageRecieveBinary(socket_client, MESSAGE_TO_KEY)
        # Send message to Server to get an IV.
        iv = lib.socketLibrary.messageRecieveBinary(socket_client, MESSAGE_TO_IV)

        # Encrypte a message
        encrypted_message = lib.encryptAES.encrypte("Thank you for key and iv".encode(), key, iv)
        # Send the encrypted message with a key and recieve an encrypted message of Client
        recieve_encrypted_message = lib.socketLibrary.messagesBinary(socket_client, encrypted_message)
        # Decrypte a message of Client with a key
        recieve_decrypted_message = lib.encryptAES.decrypte(recieve_encrypted_message, key, iv)
        recieve_decrypted_message = recieve_decrypted_message

        while recieve_decrypted_message != BYE:
        
            # Decrypte the message of Server with a key
            recieve_decrypted_message = lib.encryptAES.decrypte(recieve_encrypted_message, key, iv)
            recieve_decrypted_message = recieve_decrypted_message.decode("utf-8")
            # Print a decrypted message of Server
            print(recieve_decrypted_message)

            # Input the message
            input_message = input(MESSAGE_TO_INPUT)
            # Encrypte the input messsage
            encrypted_message = lib.encryptAES.encrypte(input_message.encode(), key, iv)
            # Send the encrypted message with a key and recieve an encrypted message of Server
            recieve_encrypted_message = lib.socketLibrary.messagesBinary(socket_client, encrypted_message)
            # Decrypte a message of Client with a key
            recieve_decrypted_message = lib.encryptAES.decrypte(recieve_encrypted_message, key, iv)
            recieve_decrypted_message = recieve_decrypted_message.decode("utf-8")


if __name__ == '__main__':
    client_program()
