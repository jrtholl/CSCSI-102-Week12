# https://github.com/jrtholl/CSCSI-102-Week12
# Jared Tholl
# CSCI 102 - Section E; 11:00am - 11:50am
# Lab: Week 12 - Part B

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
# fix the FindWordCount
def FindWordCount(x, string):
    list_words = x
    checker = string
    count = 0
    for spot in list_words:
        list_words = spot.split()
        for word in list_words:
            if string.lower() in word.lower():
                count += 1
    return count
def ScoreFinder(list_1, list_2, name):
    count = 0
    for y in list_1:
        if name.lower() != y.lower():
            count += 1
    if count != len(list_1):
        for x in range(len(list_1)):
            if name.lower() == list_1[x].lower():
                spot = x
        print('OUTPUT %s got a score of %d' %(name, list_2[spot]))
    else:
        print('OUTPUT player not found')
def Union(list_1, list_2):
    new_list = list_1 + list_2
    return new_list
def Intersection(list_1, list_2):
    new_list = []
    for x in list_1:
        if x in list_2:
            new_list.append(x)
    return new_list
def NotIn(list_1, list_2):
    new_list = []
    for x in list_1:
        if x not in list_2:
            new_list.append(x)
    return new_list
