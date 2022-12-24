words ={}
file = open('words.txt')    #Opening the file

for word in file:
    print(word)
    line=word.strip()
    words[word]=True
while True:
    if word=="done":
        break
    if word in words:
        print(word, "is in the dictionary.")
    else:
        print(word, "is not in the dictionary.")