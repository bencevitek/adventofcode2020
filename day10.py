numbers = []
with open('day10.txt') as f:
    for line in f:
        numbers.append(int(line))

numbers.sort()
numbers.append(numbers[-1] + 3)

#task1
onejolt = 0
threejolt = 0
prev = 0
for number in numbers:
    #print(number)
    if number - prev == 1:
        onejolt += 1
    elif number - prev == 3:
        threejolt += 1
    prev = number

print(onejolt * threejolt)

#task2
prev = 0
currcount = 1
final = 1
for number in numbers:
    if number - prev == 1:
        currcount += 1
    elif number - prev == 3:
        if currcount == 3:
            final = final * 2
        elif currcount == 4:
            final = final * 4
        elif currcount == 5:
            final = final * 7
        currcount = 1
    prev = number

print(final)
