import re
summ = 0

def calculate(line):
    base = int(re.search("([0-9]+)", line)[1])
    operations = re.findall("([+*])", line[len(re.search("([0-9]+)", line)[1]):])
    numbers = re.findall("([0-9]+)", line[len(re.search("([0-9]+)", line)[1]):])
    for i in range(len(numbers)):
        if operations[i] == "*":
            base *= int(numbers[i])
        else:
            base += int(numbers[i])
    return base

with open('day18.txt') as f:
    for line in f:
        while re.search("\(", line):
            find = re.search("\(([ *+0-9]+)\)", line)
            temp = calculate(find[1])
            line = line.replace("("+find[1]+")", str(temp))
        summ += calculate(line)

print(summ)

#task2
def calculate2(line):
    while re.search("\+", line):
        find = re.search("([0-9]+) \+ ([0-9]+)", line)
        temp = int(find[1]) + int(find[2])
        line = line.replace(find[1]+" + "+find[2], str(temp), 1)
    while re.search("\*", line):
        find = re.search("([0-9]+) \* ([0-9]+)", line)
        temp = int(find[1]) * int(find[2])
        line = line.replace(find[1]+" * "+find[2], str(temp), 1)
    return int(line)

summ2 = 0
with open('day18.txt') as f:
    for line in f:
        while re.search("\(", line):
            find = re.search("\(([ *+0-9]+)\)", line)
            temp = calculate2(find[1])
            line = line.replace("("+find[1]+")", str(temp))
        summ2 += calculate2(line)

print(summ2)