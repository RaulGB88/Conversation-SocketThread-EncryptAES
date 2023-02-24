
def encrypt(message, key):
    """ Encrypte with Cesar ASCI method """

    text = ''

    for letter in message:
        ascii_value = ord(letter)
        base = ord(' ')
        encrypted_value = ((ascii_value + int(key) - base) % 94) + base
        text = text + chr(encrypted_value)

        # if(cadena + key) < longitud total (122) else {- longitud vector (26)}

        #position_enrypted = int(letter_enrypted) % 26
        #text = text + str(chr(position_enrypted))

    return text


def decrypt(message, key):
    """ Decrypt with Cesar ASCI method """

    text = ''

    for letter in message:
        ascii_value = ord(letter)
        base = ord(' ')
        encrypted_value = ((ascii_value - int(key) - base) % 94) + base
        text = text + chr(encrypted_value)

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