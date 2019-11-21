# https://github.com/jrtholl/CSCSI-102-Week12
# Jared Tholl
# CSCI 102 - Section E; 11:00am - 11:50am
# Lab: Week 11 - Part B

def PrintOutput(x):
    print('OUTPUT ' + x)
def LoadFile(x):
    file = x
    lines = open(file, "r")
    lines_con = lines.readlines()
    lines.close()
    new_list = []
    for x in lines_con:
        y = ""
        for letter in x:
            if letter == "\n":
                continue
            else:
                y += letter
        new_list.append(y)
    return new_list
def UpdateString(string, letter, spot):
    new_string = ""
    for x in range(len(string)):
        if x == spot:
            new_string += letter
        else:
            new_string += string[x]
    print("OUTPUT", new_string)
def FindWordCount(x, string):
    list_words = x
    checker = string
    count = 0
    for x in list_words:
        if string in x:
            count += 1
    return count
