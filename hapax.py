import re

def hapax(file):
    file = open(file)
    words = re.findall('\w+',file.read().lower())
    freq = {key : 0 for key in words}
    for word in words:
        freq[word] += 1
        for word in freq:
            if freq[word] == 1:
                print(word)

print(hapax("alice.txt"))
