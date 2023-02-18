import codecs

def XOR(buf1, buf2):
    if not len(buf1) == len(buf2):
        return False
    buf1 = codecs.decode(buf1, 'hex')
    buf2 = codecs.decode(buf2, 'hex')

    return bytes(a ^ b for a, b in zip(buf1, buf2))

print(XOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965').hex())
# 746865206b696420646f6e277420706c6179
# the kid don't play
