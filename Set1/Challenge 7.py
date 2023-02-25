import os
import codecs
from Crypto.Cipher import AES

def main():
    message = open(os.path.join(os.getcwd(), 'Input/Set1/Input 7.txt'), 'rb').read()
    message = codecs.decode(message, 'base64')
    key = codecs.encode('YELLOW SUBMARINE', 'utf-8')

    print(decrypt_AES(message, key))

def decrypt_AES(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return codecs.decode(cipher.decrypt(message), 'utf-8')

if __name__ == '__main__':
    main()