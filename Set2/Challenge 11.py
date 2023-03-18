import secrets
import random
import codecs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def gen_ran_AES(size):
    return secrets.token_bytes(size)

def gen_ran_bytes(min, max):
    size = random.randint(min, max) 
    return secrets.token_bytes(size)


def encryption_oracle(message):
    key = gen_ran_AES(16)

    appended_message = gen_ran_bytes(5, 10) + codecs.encode(message, 'utf-8') + gen_ran_bytes(5, 10)
    appended_message = pad(appended_message, 16)

    if random.randint(0, 1):
        cipher = AES.new(key, AES.MODE_ECB)
        print('Used ECB')
    else:
        cipher = AES.new(key, AES.MODE_CBC, gen_ran_AES(16))
        print('Used CBC')
    
    return cipher.encrypt(appended_message)

def detect_encryption():
    # The trick here is that ecb is deterministic so if we feed it blocks with the same data
    blob = 'lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll'
    
    message = encryption_oracle(blob)
    message_chunks = [message[i:i+8] for i in range(0, len(message), 8)]
    
    # It should have encrypted blocks which are identical
    if len(set(message_chunks)) == len(message_chunks):
        return 'The encryption function used CBC'
    return 'The encryption function used ECB'  

def main():
    # print(gen_ran_AES(16))

    # encrypted_data = encryption_oracle('This is also test input, randomise me')
    # print(encrypted_data)

    print(detect_encryption())

if __name__ == '__main__':
    main()