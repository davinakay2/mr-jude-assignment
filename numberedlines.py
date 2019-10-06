def numberlines(file,newfile):
    temp = ""
    numb = 1
    for line in open(file):
        temp += f"{numb} {line}"
        numb += 1
    with open(newfile, "w+") as handler:
        handler.write(temp)

numberlines("kayla.txt","kaylanew.txt")