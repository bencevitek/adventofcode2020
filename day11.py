#task1
seatlines = []
seatlines.append(["L"] * 100)
with open('day11.txt') as f:
    for line in f:
        seatlines.append(list("L"+line[:-1]+"L"))
seatlines.append(["L"] * 100)

reservedseats = 0
for x in range(1,len(seatlines)-1):
    for y in range(1,len(seatlines[0])-1):
        if seatlines[x][y] == "L":
            seatlines[x][y] = "#"
            reservedseats += 1

templines = [x[:] for x in seatlines]

changed = True

while changed:
    changed = False
    for x in range(1,len(seatlines)-1):
        for y in range(1,len(seatlines[0])-1):
            if seatlines[x][y] == "L":
                if seatlines[x-1][y-1] != "#" and seatlines[x-1][y] != "#" and seatlines[x-1][y+1] != "#" and seatlines[x][y-1] != "#" and seatlines[x][y+1] != "#" and seatlines[x+1][y-1] != "#" and seatlines[x+1][y] != "#" and seatlines[x+1][y+1] != "#":
                    templines[x][y] = "#"
                    reservedseats += 1
                    changed = True
            elif seatlines[x][y] == "#":
                counter = 0
                if seatlines[x-1][y-1] == "#":
                    counter += 1
                if seatlines[x-1][y] == "#":
                    counter += 1
                if seatlines[x-1][y+1] == "#":
                    counter += 1
                if seatlines[x][y-1] == "#":
                    counter += 1
                if seatlines[x][y+1] == "#":
                    counter += 1
                if seatlines[x+1][y-1] == "#":
                    counter += 1
                if seatlines[x+1][y] == "#":
                    counter += 1
                if seatlines[x+1][y+1] == "#":
                    counter += 1
                if counter > 3:
                    templines[x][y] = "L"
                    reservedseats -= 1
                    changed = True
    seatlines = [x[:] for x in templines]

print(reservedseats)

#task2
seatlines = []
reservedseats = 0
with open('day11.txt') as f:
    for line in f:
        seatlines.append(list(line[:-1]))

for x in range(0,len(seatlines)):
    for y in range(0,len(seatlines[0])):
        if seatlines[x][y] == "L":
            seatlines[x][y] = "#"
            reservedseats += 1

templines = [x[:] for x in seatlines]

def checkforreserved(x, y):
    count = 0
    if x < len(seatlines)-1:
        for n in range(x+1, len(seatlines[0])):
            if seatlines[n][y] == "#":
                count += 1
                break
            if seatlines[n][y] == "L":
                break
    if x > 0:
        for n in range(x-1, -1, -1):
            if seatlines[n][y] == "#":
                count += 1
                break
            if seatlines[n][y] == "L":
                break
    if y < len(seatlines[0])-1:
        for n in range(y+1, len(seatlines)):
            if seatlines[x][n] == "#":
                count += 1
                break
            if seatlines[x][n] == "L":
                break
    if y > 0:
        for n in range(y-1, -1, -1):
            if seatlines[x][n] == "#":
                count += 1
                break
            if seatlines[x][n] == "L":
                break
    a = x-1
    b = y-1
    while a >= 0 and b >= 0:
        if seatlines[a][b] == "#":
            count +=1
            break
        if seatlines[a][b] == "L":
            break
        a -= 1
        b -= 1
    
    a = x-1
    b = y+1
    while a >= 0 and b <= len(seatlines[0])-1:
        if seatlines[a][b] == "#":
            count +=1
            break
        if seatlines[a][b] == "L":
            break
        a -= 1
        b += 1

    a = x+1
    b = y-1
    while a <= len(seatlines)-1 and b >= 0:
        if seatlines[a][b] == "#":
            count +=1
            break
        if seatlines[a][b] == "L":
            break
        a += 1
        b -= 1

    a = x+1
    b = y+1
    while a <= len(seatlines)-1 and b <= len(seatlines[0])-1:
        if seatlines[a][b] == "#":
            count +=1
            break
        if seatlines[a][b] == "L":
            break
        a += 1
        b += 1

    if count > 4:
        return 1
    else:
        return 0

def checkforempty(x,y):
    if x < len(seatlines)-1:
        for n in range(x+1, len(seatlines[0])):
            if seatlines[n][y] == "#":
                return 0
            if seatlines[n][y] == "L":
                break
    if x > 0:
        for n in range(x-1, -1, -1):
            if seatlines[n][y] == "#":
                return 0
            if seatlines[n][y] == "L":
                break
    if y < len(seatlines[0])-1:
        for n in range(y+1, len(seatlines)):
            if seatlines[x][n]== "#":
                return 0
            if seatlines[x][n] == "L":
                break
    if y > 0:
        for n in range(y-1, -1, -1):
            if seatlines[x][n] == "#":
                return 0
            if seatlines[x][n] == "L":
                break

    a = x-1
    b = y-1
    while a >= 0 and b >= 0:
        if seatlines[a][b] == "#":
            return 0
        if seatlines[a][b] == "L":
            break
        a -= 1
        b -= 1
    
    a = x-1
    b = y+1
    while a >= 0 and b <= len(seatlines[0])-1:
        if seatlines[a][b] == "#":
            return 0
        if seatlines[a][b] == "L":
            break
        a -= 1
        b += 1

    a = x+1
    b = y-1
    while a <= len(seatlines)-1 and b >= 0:
        if seatlines[a][b] == "#":
            return 0
        if seatlines[a][b] == "L":
            break
        a += 1
        b -= 1

    a = x+1
    b = y+1
    while a <= len(seatlines)-1 and b <= len(seatlines[0])-1:
        if seatlines[a][b] == "#":
            return 0
        if seatlines[a][b] == "L":
            break
        a += 1
        b += 1

    return 1

changed = True
while changed:
    changed = False
    for x in range(0,len(seatlines)):
        for y in range(0,len(seatlines[0])):
            if seatlines[x][y] == "#" and checkforreserved(x,y):
                templines[x][y] = "L" 
                reservedseats -= 1
                changed = True
            elif seatlines[x][y] == "L" and checkforempty(x,y):
                templines[x][y] = "#"
                reservedseats += 1
                changed = True
    seatlines = [x[:] for x in templines]

print(reservedseats)