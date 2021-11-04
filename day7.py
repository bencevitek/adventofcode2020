import re
count = []
count2 = 0

def check(lines,target):
    global count
    for line in lines:
        if re.search("^([a-z ]+) bags contain.*[1-9] "+target, line):
            match = re.search("^([a-z ]+) bags contain.*[1-9] "+target, line)
            if(match.group(1) not in count):
                count.append(match.group(1))
                check(lines,match.group(1))


def check2(lines,target,multi):
    global count2
    for line in lines:
        if re.search("^"+ target +" bags contain ", line):
            match = re.search("^"+ target +" bags contain (.*)", line)
            if(match.group(1) != "no other bags."):
                y = match.group(1).split(",")
                for bag in y:
                    color = re.search("([1-9]) ([a-z ]+) bag", bag)
                    count2 += multi*int(color.group(1))
                    check2(lines,color.group(2),multi*int(color.group(1)))


lines = []
with open('day7.txt') as f:
    for line in f:
        lines.append(line)

#task1
check(lines,"shiny gold")
print(len(count))

#task2
check2(lines,"shiny gold",1)
print(count2)




        


