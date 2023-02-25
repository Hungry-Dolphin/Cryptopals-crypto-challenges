import os 
import codecs 
from Crypto.Cipher import AES

def main():
    messages = open(os.path.join(os.getcwd(), 'Input/Set1/Input 8.txt'), 'r').read().split('\n')
    messages = [ codecs.decode(x, 'hex') for x in messages ]

    for message in messages:
        n = 16
        blocks = [message[i:i+n] for i in range(0, len(message), n)]

        if len(blocks) != len(set(blocks)):
            print(message)


if __name__ == '__main__':
    main()