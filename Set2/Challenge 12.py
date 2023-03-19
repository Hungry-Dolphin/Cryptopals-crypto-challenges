import secrets
import random
import codecs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY = secrets.token_bytes(16)

def gen_ran_bytes(min, max):
    size = random.randint(min, max) 
    return secrets.token_bytes(size)

def encryption_oracle(message):
    string = b'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
    cipher = AES.new(KEY, AES.MODE_ECB)
    # A bit cramped so I don't spoil myself with the base64 decode while debugging
    return cipher.encrypt(pad(codecs.encode(message, 'utf-8') + codecs.decode(string, 'base64'), 16))

def det_block_size():
    # I realised that they probs want you to make the input bigger untill you see another block
    # This way you know how big the block size is 
    # My function only works when ECB is used. ¯\_(ツ)_/¯
    for x in range(50):
        message = encryption_oracle('x'*x)
        message_chunks = [message[i:i+8] for i in range(0, len(message), 8)]
        if len(set(message_chunks)) != len(message_chunks):
            # Found the block size
            return int(x / 2)

def decrypt_byte(input_block, b_s, m, b_n):
    characters = [i for i in range(128)] 
    chr_dict = dict()
    for ch in characters:
        message = encryption_oracle(input_block+m+chr(ch))[b_n*b_s:(b_n+1)*b_s]
        chr_dict[str(chr(ch))] = message

    enc_char = encryption_oracle(input_block)[b_n*b_s:(b_n+1)*b_s]
    for item, value in chr_dict.items():
        if enc_char == value:
            return item

def ECB_decryptor():
    # Determine block size
    block_size = det_block_size()

    message = ''
    block_amount = int((len(encryption_oracle(''))/block_size))
    for block in range(0, block_amount):
        for x in range(block_size):
            input_block = 'x'*(block_size-(1+x))

            letter = decrypt_byte(input_block, block_size, message, block)
            # Since we dont know when the padding begins we make the assumption
            # That the first letter we cant decrypt on the last block is the start of the padding
            if block == block_amount-1 and not letter:
                break
            message += letter

    print(message)

def main():
    # print(encryption_oracle('This is a message'))
    ECB_decryptor()

if __name__ == '__main__':
    main()


