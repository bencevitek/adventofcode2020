commands = []
with open('day8.txt') as f:
    for line in f:
        commands.append(line)

#task1
accumulator = 0
second = False
usedcommands = []
current = 0
while not second:
    y = commands[current].split(" ")
    usedcommands.append(current)
    if y[0] == "nop":
        current += 1
    elif y[0] == "acc":
        current += 1
        if y[1][0] == "+":
            accumulator += int(y[1][1:])
        else:
            accumulator -= int(y[1][1:])
    else:
        if y[1][0] == "+":
            current += int(y[1][1:])
        else:
            current -= int(y[1][1:])
    if current in usedcommands:
        second = True

print(accumulator)

#task2
accumulator = 0
second = False
usedcommands = []
current = 0
winner = len(commands) - 1
finished = False
usedchanges = []
changed = False
while not finished:
    second = False
    while not second:
        y = commands[current].split(" ")
        usedcommands.append(current)
        if not changed and y[0] != "acc" and commands[current] not in usedchanges:
            if(y[0] == "nop"):
                y[0] = "jmp"
            elif(y[0] == "jmp"):
                y[0] = "nop"
            changed = True
            usedchanges.append(commands[current])
        if y[0] == "nop":
            current += 1
        elif y[0] == "acc":
            current += 1
            if(y[1][0] == "+"):
                accumulator += int(y[1][1:])
            else:
                accumulator -= int(y[1][1:])
        else:
            if(y[1][0] == "+"):
                current += int(y[1][1:])
            else:
                current -= int(y[1][1:])
        if current in usedcommands:
            second = True
            accumulator = 0
            usedcommands.clear()
            current = 0
            changed = False
        if current == winner:
            second = True
            finished = True

print(accumulator)