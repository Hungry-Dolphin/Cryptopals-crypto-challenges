from Crypto.Util.Padding import pad
import codecs

def main():
    message = codecs.encode('YELLOW SUBMARINE', 'utf-8')
    print(pad(message, 20))

if __name__ == '__main__':
    main()