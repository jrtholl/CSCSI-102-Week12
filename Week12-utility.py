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
