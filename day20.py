import re
tiledict = {}
up = ""
down = ""
left = ""
right = ""
linecounter = 1
with open('day201.txt') as f:
    for line in f:
        if re.match("Tile",line):
            tileid = re.match("Tile ([0-9]+):",line)[1]
            tiledict[tileid] = []
        elif line == '\n':
            tiledict[tileid].append(up)
            tiledict[tileid].append(right)
            tiledict[tileid].append(down)
            tiledict[tileid].append(left)
            linecounter = 1
            up = ""
            down = ""
            left = ""
            right = ""
        else:
            if linecounter == 1:
                up = line[:-1]
            if linecounter == 10:
                down = line[:-1]
            left = left + line[0]
            right = right + line[-2]
            linecounter += 1

answer = 1
directionarray = ["up", "right", "down", "left"]
for tile in tiledict:
    counter = 0
    for index,border in enumerate(tiledict[tile]):
        for insidetile in tiledict:
            if tile != insidetile:
                if border == tiledict[insidetile][0]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" up:"+tiledict[insidetile][0])
                    counter += 1
                if border == tiledict[insidetile][1]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" right:"+tiledict[insidetile][1])
                    counter += 1
                if border == tiledict[insidetile][2]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" down:"+tiledict[insidetile][2])
                    counter += 1
                if border == tiledict[insidetile][3]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" left:"+tiledict[insidetile][3])
                    counter += 1
                if border == tiledict[insidetile][0][::-1]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" reverseup:"+tiledict[insidetile][0])
                    counter += 1
                if border == tiledict[insidetile][1][::-1]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" reverseright:"+tiledict[insidetile][1])
                    counter += 1
                if border == tiledict[insidetile][2][::-1]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" reversedown:"+tiledict[insidetile][2])
                    counter += 1
                if border == tiledict[insidetile][3][::-1]:
                    print("id:"+tile+" direction: "+directionarray[index]+" othertileid:"+insidetile+" reverseleft:"+tiledict[insidetile][3])
                    counter += 1
    if counter == 2:
        answer *= int(tile)

print(answer)