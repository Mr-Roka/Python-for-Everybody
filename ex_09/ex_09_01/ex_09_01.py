words ={}
file = open('words.txt')    #Opening the file

for word in file:
    #print(word)
    line=word.strip()
    words[word]=None

#print(words)

if "hello" in words:
    print("hello", "is in the dictionary.")
else:
    print("hello", "is not in the dictionary.")   