import os
from Crypto.Cipher import AES

""" ---- ENCRYPT AES METHODS ---- """
def generateKeys(message):
    """Generate Keys for AES encrypte and decrypte """

    mensaje = formatear_multiplo_de_16(message)

    key = os.urandom(16) #establecemos una clave de 16 bytes
    iv = os.urandom(AES.block_size) #generamos aleatoriamente un iv del tamaño del bloque AES

    messageEncrypted = encrypte(message, key, iv)  # para imprimir una mejor representación
    #messageEncrypted_decod = base64.b64encode(messageEncrypted).decode("utf-8")

    return messageEncrypted, key, iv


def encrypte(message,key,iv):
    """ Encrypte with AES method """

    #instanciamos un nuevo objeto AES
    cipher = AES.new(key,AES.MODE_OFB,IV=iv)
    #ciframos los datos
    bytesEncrypted = cipher.encrypt(message)

    return bytesEncrypted


def decrypte(message,key,iv):
    """ Decrypte with AES method """

    #es necesario un nuevo objeto para descifrar
    cipher = AES.new(key, AES.MODE_OFB,IV=iv)
    messageDecrypted = cipher.decrypt(message)

    return messageDecrypted


def formatear_multiplo_de_16(text):
    """ Formatea el mensaje para encriptarlo con el método César """

    while (len(text) % 16 != 0):
        text += b' '  # leañado espacios en blanco al final

    return text