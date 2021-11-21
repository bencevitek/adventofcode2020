import re
memdict = {}
with open('day14.txt') as f:
    for line in f:
        temp = ""
        if line[1] == "a":
            mask = line[7:-1]
        else:
            match = re.search("mem.([0-9]+). = ([0-9]+)", line)
            place = match[1]
            binversion = "{0:036b}".format(int(match[2]))
            for index, byte in enumerate(mask, start=0):
                if byte == "1" or byte == "0":
                    temp += byte
                else:
                    temp += binversion[index]
            memdict[place] = int(temp,2)

sum = 0
for item in memdict:
    sum += memdict[item]

print(sum)

#task2
from itertools import product
memdict = {}
def calculatevariations(bin, value):
    #indexes = [x for x, v in enumerate(bin) if v == 'X']
    variationlist = list(map(list,product([0, 1], repeat=bin.count("X"))))
    for arrs in variationlist:
        temp = bin
        for num in arrs:
            temp = temp.replace( "X", str(num), 1)
        memdict[int(temp,2)] = int(value)

with open('day14.txt') as f:
    for line in f:
        temp = ""
        if line[1] == "a":
            mask = line[7:-1]
        else:
            match = re.search("mem.([0-9]+). = ([0-9]+)", line)
            value = match[2]
            binversion = "{0:036b}".format(int(match[1]))
            for index, byte in enumerate(mask, start=0):
                if byte == "1" or byte == "X":
                    temp += byte
                else:
                    temp += binversion[index]
            calculatevariations(temp, value)

sum = 0
for item in memdict:
    sum += memdict[item]

print(sum)