def repeating_key_XOR(message, key):
    message_ord = [ord(x) for x in message]
    key_list = [x for x in key]
    index = 0
    encoded = list()

    for x in message_ord:
        if index < len(key_list):
            encoded.append(x ^ ord(key_list[index]))
            index += 1 
        else:
            encoded.append(x ^ ord(key_list[0]))
            index = 1             
    return ''.join([hex(x)[2:].zfill(2) for x in encoded])

message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

print(repeating_key_XOR(message, key))
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
# It has a different character for newline, I wonder why