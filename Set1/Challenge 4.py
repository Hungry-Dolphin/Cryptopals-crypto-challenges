import codecs
import os 

# Read messages
messages = open(os.path.join(os.getcwd(), 'Input/Set1/Input 4.txt'), 'r').read().split('\n')
# Decode hex
decoded_messages = [codecs.decode(x, 'hex') for x in messages]

# get all characters it could have been XORed with 
characters = [i for i in range(128)] 
letters = [chr(i) for i in range(97, 123)]  # do chr(i) to get the letters
# Save all possible options in a dictonary
outcomes = dict()

for message in decoded_messages:
    for ch in characters:
        # XOR with character
        attempt = [ x ^ ch for x in message ]
        # For each character that is a lower case letter append 1
        score = sum([1 if chr(item) in letters else 0 for item in attempt])
        # Save the answer and the score to a dictonary
        # I already translate the bytearray to a string since it would not save in a dictonary otherwise
        outcomes[''.join([chr(x) for x in attempt])] = score 

# Show the outcome with the highest score
print(max(outcomes, key=outcomes.get))
# Now that the party is jumping