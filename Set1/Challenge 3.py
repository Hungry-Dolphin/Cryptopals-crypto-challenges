import codecs

message = codecs.decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', 'hex')
# get all characters it could have been XORed with 
characters = [i for i in range(128)] 
letters = [chr(i) for i in range(97, 123)]  # do chr(i) to get the letters
# Save all possible options in a dictonary
outcomes = dict()

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
# Cooking MC's like a pound of bacon