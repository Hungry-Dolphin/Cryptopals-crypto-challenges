import codecs
import os 

def compute_ham(string1, string2):
    # Check if strings are equal length
    if len(string1) != len(string2):
        return None

    # Convert string to bits
    if type(string1) == bytes: 
        bit_string1 = ''.join([bin(x)[2:].zfill(8) for x in string1])
    else:
        bit_string1 = ''.join([bin(ord(x))[2:].zfill(8) for x in string1])
    
    if type(string2) == bytes: 
        bit_string2 = ''.join([bin(x)[2:].zfill(8) for x in string2])
    else:
        bit_string2 = ''.join([bin(ord(x))[2:].zfill(8) for x in string2])

    # Compute hamming distance
    count = 0 
    for index, value in enumerate(bit_string1):
        count += 0 if value == bit_string2[index] else 1

    # Return hamming distance
    return count

def return_likey_xor_key_length(KEYSIZES, message):
    distances = dict()

    for key in KEYSIZES:
        one = message[:key]
        two = message[key:key*2]
        three = message[key*2:key*3]
        four = message[key*3:key*4]
        #distances[key] = compute_ham(one, two)/key
        distances[key] = (compute_ham(one, two)/key + compute_ham(two, three)/key + compute_ham(three, four)/key)/3

    return dict(sorted(distances.items(), key = lambda x: x[1])[:3])

def solve_single_XOR(block):
    # get all characters it could have been XORed with 
    characters = [i for i in range(128)] 
    
    # My original code for doing this 
    # letters = [chr(i) for i in range(65, 91)]  # do chr(i) to get the letters
    # letters = letters + [chr(i) for i in range(97, 123)]
    # letters2 = [chr(i) for i in range(32, 128)]

    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    
    # Save all possible options in a dictonary
    outcomes = dict()

    for ch in characters:
        # XOR with character
        attempt = [x ^ ch for x in block]
        
        # score = sum([1 if chr(item) in letters else 0 for item in attempt])
        # score = sum([1 if chr(item) in letters2 else 0 for item in attempt])
        # score = sum([1 if chr(item).upper() in ['E', 'A', 'I', 'O'] else 0 for item in attempt])

        score = sum([character_frequencies.get(chr(byte).lower(), 0) for byte in attempt])

        outcomes[f'{chr(ch)}'] = score

    # Return item with highest score:
    return max(outcomes, key=outcomes.get)

def repeating_key_XOR(message, key):
    
    message_ord = [x for x in message] if type(message[0]) == int else [ord(x) for x in message]
    key_ord = [x for x in key] if type(key[0]) == int else [ord(x) for x in key]
    index = 0
    decoded = list()

    for x in message_ord:
        if index < len(key_ord):
            decoded.append(chr(x ^ key_ord[index]))
            index += 1 
        else:
            decoded.append(chr(x ^ key_ord[0]))
            index = 1             
    return ''.join([str(x) for x in decoded])

def break_repeating_key_XOR(message):

    KEYSIZES = [x for x in range(2, 41)]
    key_lengths = return_likey_xor_key_length(KEYSIZES, message).keys()
    # Key length is most likely 29

    for length in key_lengths:
        split_message = [message[i:i+length] for i in range(0, len(message), length)]
        blocks = list()

        for index in range(0, length):
            # blocks.append([x[index] for x in split_message])
            transpose = list()

            for char_block in split_message:
                try:
                    transpose.append(char_block[index])
                except IndexError:
                    continue

            blocks.append(transpose)
        
        key_list = [solve_single_XOR(block) for block in blocks]
        key = ''.join(key_list)
        
        print()
        print(f'Key == {key}')
        print(repeating_key_XOR(message, key))


def main():
    message = open(os.path.join(os.getcwd(), 'Input/Set1/Input 6.txt'), 'rb').read()
    message = codecs.decode(message, 'base64')


    # print(compute_ham("this is a test", "wokka wokka!!!"))
    # 37
    
    break_repeating_key_XOR(message)
    

if __name__ == '__main__':
    main()
