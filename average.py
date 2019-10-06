import re

def average(filename):
    file = open(filename)
    words = re.findall('\w+',file.read())
    total = sum([len(word) for word in words])
    length = len(words)
    return int(total/length)

print(average("alice.txt"))