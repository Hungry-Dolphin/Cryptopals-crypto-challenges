import os
import codecs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def main():
    message = open(os.path.join(os.getcwd(), 'Input/Set2/Input 10.txt'), 'rb').read()
    # message = b'This is a message I use to test stuff, it has to be long enough'
    key = codecs.encode('YELLOW SUBMARINE', 'utf-8')
    iv = b''.join([b'\x00' for x in range(0, 16)])

    # a = encrypt_AES_CBC(message, key, iv)
    # print(a)
    # b = decrypt_AES_CBC(a, key, iv)
    # print(b)

    print(decrypt_AES_CBC(codecs.decode(message, 'base64'), key, iv))

def encrypt_AES_CBC(message, key, iv):
    blocks = [message[i:i+16] for i in range(0, len(message), 16)]
    enc_message = b''
    last_block = None
    
    for block in blocks:
        if len(block) != 16:
            block = pad(block, 16)
        if not last_block:
            combine = [block[x] ^ iv[x] for x in range(0, 16)]
        else:
            combine = [block[x] ^ last_block[x] for x in range(0, 16)]
        
        enc = encrypt_AES_ECB(bytes(combine), key)
        last_block = enc
        enc_message += enc

    return enc_message

def decrypt_AES_CBC(message, key, iv):
    blocks = [message[i:i+16] for i in range(0, len(message), 16)]
    enc_message = b''
    last_block = None

    for index, block in enumerate(blocks) :
        enc = decrypt_AES_ECB(block, key)

        if not last_block:
            combine = [enc[x] ^ iv[x] for x in range(0, 16)]
            last_block = True
        else:
            combine = [enc[x] ^ blocks[index-1][x] for x in range(0, 16)]
        
        
        enc_message += bytes(combine)

    return unpad(enc_message, 16)

def encrypt_AES_ECB(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(message)

def decrypt_AES_ECB(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(message)

if __name__ == '__main__':
    main()