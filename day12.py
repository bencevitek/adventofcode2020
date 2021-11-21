commands = []
with open('day12.txt') as f:
    for command in f:
        commands.append(command)

directions = []
directions += ["E","S","W","N"] * 30
currentdirection = 8
curreastwest = "E"
curreastwestvalue = 0
currnorthsouth = "N"
currnorthsouthvalue = 0
for command in commands:
    if command[0] == "L":
        currentdirection -= int(int(command[1:])/90)
    elif command[0] == "R":
        currentdirection += int(int(command[1:])/90)
    elif command[0] == "E" or (command[0] == "F" and directions[currentdirection] == "E"):
        if curreastwest == "E":
            curreastwestvalue += int(command[1:])
        elif curreastwest == "W":
            curreastwestvalue -= int(command[1:])
            if curreastwestvalue < 0:
                curreastwest = "E"
                curreastwestvalue = abs(curreastwestvalue)
    elif command[0] == "W" or (command[0] == "F" and directions[currentdirection] == "W"):
        if curreastwest == "W":
            curreastwestvalue += int(command[1:])
        elif curreastwest == "E":
            curreastwestvalue -= int(command[1:])
            if curreastwestvalue < 0:
                curreastwest = "W"
                curreastwestvalue = abs(curreastwestvalue)
    elif command[0] == "S" or (command[0] == "F" and directions[currentdirection] == "S"):
        if currnorthsouth == "S":
            currnorthsouthvalue += int(command[1:])
        elif currnorthsouth == "N":
            currnorthsouthvalue -= int(command[1:])
            if currnorthsouthvalue < 0:
                currnorthsouth = "S"
                currnorthsouthvalue = abs(currnorthsouthvalue)
    elif command[0] == "N" or (command[0] == "F" and directions[currentdirection] == "N"):
        if currnorthsouth == "N":
            currnorthsouthvalue += int(command[1:])
        elif currnorthsouth == "S":
            currnorthsouthvalue -= int(command[1:])
            if currnorthsouthvalue < 0:
                currnorthsouth = "N"
                currnorthsouthvalue = abs(currnorthsouthvalue)

print(curreastwestvalue+currnorthsouthvalue)

#task2
directions = []
directions += ["E","S","W","N"] * 50
waypointdir1 = 12
waypointvalue1 = 10
waypointdir2 = 11
waypointvalue2 = 1
shipeastwest = "E"
shipeastwestvalue = 0
shipnorthsouth = "N"
shipnorthsouthvalue = 0

def movewaypoint(dir1, dir2, value):
    global waypointdir1, waypointvalue1, waypointdir2, waypointvalue2
    if directions[waypointdir1] == dir1:
        waypointvalue1 += value
    elif directions[waypointdir1] == dir2:
        waypointvalue1 -= value
        if waypointvalue1 < 0:
            waypointdir1 = waypointdir1 + 2 if waypointdir1 < 25 else waypointdir1 - 2
            waypointvalue1 = abs(waypointvalue1)
    elif directions[waypointdir2] == dir1:
        waypointvalue2 += value
    elif directions[waypointdir2] == dir2:
        waypointvalue2 -= value
        if waypointvalue2 < 0:
            waypointdir2 = waypointdir2 + 2 if waypointdir2 < 25 else waypointdir2 - 2
            waypointvalue2 = abs(waypointvalue2)

for command in commands:
    if command[0] == "L":
        waypointdir1 -= int(int(command[1:])/90)
        waypointdir2 -= int(int(command[1:])/90)
    elif command[0] == "R":
        waypointdir1 += int(int(command[1:])/90)
        waypointdir2 += int(int(command[1:])/90)
    elif command[0] == "E":
        movewaypoint("E", "W", int(command[1:]))
    elif command[0] == "W":
        movewaypoint("W", "E", int(command[1:]))
    elif command[0] == "S":
        movewaypoint("S", "N", int(command[1:]))
    elif command[0] == "N":
        movewaypoint("N", "S", int(command[1:]))
    elif command[0] == "F":
        multiplier = int(command[1:])
        if directions[waypointdir1] == "E" or directions[waypointdir1] == "W":
            if directions[waypointdir1] == shipeastwest:
                shipeastwestvalue += multiplier * waypointvalue1
            else:
                shipeastwestvalue -= multiplier * waypointvalue1
                if shipeastwestvalue < 0:
                    shipeastwest = directions[waypointdir1]
                    shipeastwestvalue = abs(shipeastwestvalue)
        if directions[waypointdir2] == "E" or directions[waypointdir2] == "W":
            if directions[waypointdir2] == shipeastwest:
                shipeastwestvalue += multiplier * waypointvalue2
            else:
                shipeastwestvalue -= multiplier * waypointvalue2
                if shipeastwestvalue < 0:
                    shipeastwest = directions[waypointdir2]
                    shipeastwestvalue = abs(shipeastwestvalue)
        if directions[waypointdir1] == "S" or directions[waypointdir1] == "N":
            if directions[waypointdir1] == shipnorthsouth:
                shipnorthsouthvalue += multiplier * waypointvalue1
            else:
                shipnorthsouthvalue -= multiplier * waypointvalue1
                if shipnorthsouthvalue < 0:
                    shipnorthsouth = directions[waypointdir1]
                    shipnorthsouthvalue = abs(shipnorthsouthvalue)
        if directions[waypointdir2] == "S" or directions[waypointdir2] == "N":
            if directions[waypointdir2] == shipnorthsouth:
                shipnorthsouthvalue += multiplier * waypointvalue2
            else:
                shipnorthsouthvalue -= multiplier * waypointvalue2
                if shipnorthsouthvalue < 0:
                    shipnorthsouth = directions[waypointdir2]
                    shipnorthsouthvalue = abs(shipnorthsouthvalue)

print(shipnorthsouthvalue+shipeastwestvalue)