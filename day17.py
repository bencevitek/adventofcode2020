from itertools import product
inputarr = []
fillerarraytask1 = []
for i in range(22):
    fillerarraytask1.append("......................")
for i in range(8):
    inputarr.append(fillerarraytask1)
inputarr.append(
        ["......................",
        "......................",
        "......................",
        "......................",
        "......................",
        "......................",
        "......................",
        ".......#.#..#.#.......",
        ".......#..............",
        ".......####..#........",
        "........#.#.##........",
        ".........#..#.........",
        ".......###..##........",
        "........#..##.#.......",
        "............#.........",
        "......................",
        "......................",
        "......................",
        "......................",
        "......................",
        "......................",
        "......................"])
for i in range(8):
    inputarr.append(fillerarraytask1)
active = 26
inputarrfortask2 = [x[:] for x in inputarr]

def checkreserved(z, x, y):
    count = 0
    variationlist = product([-1,0,1], repeat=2)
    for variation in variationlist:
        if not (variation[0] == 0 and variation[1] == 0) and inputarr[z][x+variation[0]][y+variation[1]] == "#":
            count += 1
        if inputarr[z+1][x+variation[0]][y+variation[1]] == "#":
            count += 1
        if inputarr[z-1][x+variation[0]][y+variation[1]] == "#":
            count += 1
    return count

for i in range(6):
    temparray = []
    temparray.append(fillerarraytask1)
    for z in range(1,len(inputarr)-1):
        tempdim = []
        tempdim.append("......................")
        for x in range(1,len(inputarr[z])-1):
            templine = "."
            for y in range(1,len(inputarr[z][x])-1):
                counter = checkreserved(z, x, y)
                if inputarr[z][x][y] == ".":
                    if counter == 3:
                        templine += "#"
                        active += 1
                    else:
                        templine += "."
                if inputarr[z][x][y] == "#":
                    if counter == 3 or counter == 2:
                        templine += "#"
                    else:
                        templine += "."
                        active -= 1
            templine += "."
            tempdim.append(templine)
        tempdim.append("......................")
        temparray.append(tempdim)
    temparray.append(fillerarraytask1)
    inputarr = [x[:] for x in temparray]
print(active)

#task2
brutalarray = []
fillerarray = []
for i in range(17):
    fillerarray.append(fillerarraytask1)

for i in range(17):
    if i != 8:
        brutalarray.append(fillerarray)
    else:
        brutalarray.append(inputarrfortask2)

active2 = 26

def checkreserved2(w, z, x, y):
    count = 0
    for i in range(-1,2):
        variationlist = product([-1,0,1], repeat=2)
        for variation in variationlist:
            if not (variation[0] == 0 and variation[1] == 0 and i == 0) and brutalarray[w+i][z][x+variation[0]][y+variation[1]] == "#":
                count += 1
            if brutalarray[w+i][z+1][x+variation[0]][y+variation[1]] == "#":
                count += 1
            if brutalarray[w+i][z-1][x+variation[0]][y+variation[1]] == "#":
                count += 1
    return count

for i in range(6):
    tempbrutalarray = []
    tempbrutalarray.append(fillerarray)
    for w in range(1, len(brutalarray)-1):
        temparray = []
        temparray.append(fillerarraytask1)
        for z in range(1,len(brutalarray[w])-1):
            tempdim = []
            tempdim.append("......................")
            for x in range(1,len(brutalarray[w][z])-1):
                templine = "."
                for y in range(1,len(brutalarray[w][z][x])-1):
                    counter = checkreserved2(w, z, x, y)
                    if brutalarray[w][z][x][y] == ".":
                        if counter == 3:
                            templine += "#"
                            active2 += 1
                        else:
                            templine += "."
                    if brutalarray[w][z][x][y] == "#":
                        if counter == 3 or counter == 2:
                            templine += "#"
                        else:
                            templine += "."
                            active2 -= 1
                templine += "."
                tempdim.append(templine)
            tempdim.append("......................")
            temparray.append(tempdim)
        temparray.append(fillerarraytask1)
        tempbrutalarray.append(temparray)
    tempbrutalarray.append(fillerarray)
    brutalarray = [x[:] for x in tempbrutalarray]
print(active2)