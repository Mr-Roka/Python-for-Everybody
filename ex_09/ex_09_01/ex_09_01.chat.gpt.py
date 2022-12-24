# Open the words.txt file
with open('words.txt', 'r') as f:
    # Create an empty dictionary
    word_dict = {}

    # Read each line in the file
    for line in f:
        # Strip the leading and trailing whitespace from the line
        word = line.strip()

        # Add the word to the dictionary as a key
        # The value is not important, so we can set it to anything
        word_dict[word] = None
print(word_dict)

# Now the dictionary contains all the words in the file as keys
# We can use the in operator to check whether a word is in the dictionary
if 'hello' in word_dict:
    print('The word "hello" is in the dictionary')
else:
    print('The word "hello" is not in the dictionary')
