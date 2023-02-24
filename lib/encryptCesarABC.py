abc='?. abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ'   

def encrypt(message, key):
    """ Encrypte with Cesar ABC method """

    text = ''

    for letter in message:
        suma = abc.find(letter) + int(key)
        module = int(suma) % len(abc)
        text = text + str(abc[module])

    return text


def decrypt(message, key):
    """ Decrypt with Cesar ABC method """

    text = ''

    for letra in message:
        suma = abc.find(letra) - int(key)
        modulo = int(suma) % len(abc)
        text = text + str(abc[modulo])

    return text


def main():
    message_decrypted = str(input('message to encrypt: ')).lower()
    key1 = str(input('key numérica: ')).lower()
    message_encypted = encrypt(message_decrypted, key1)
    print(message_encypted)

    message_encypted = str(input('message to decrypt: ')).lower()
    key2 = str(input('key numérica: ')).lower()
    message_decrypted = decrypt(message_encypted, key2)
    print(message_decrypted)


if __name__ == '__main__':
    main()