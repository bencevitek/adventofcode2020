import math

#task1
columnlow = 0
columnhigh = 127
rowlow = 0
rowhigh = 7
seatID = 0
seats = []

with open('day5.txt') as f:
    for line in f:
        sub1 = line[0:7]
        sub2 = line[7:10]
        for char in sub1:
            if char == 'B':
                columnlow = columnlow + math.ceil((columnhigh - columnlow)/2)
            else:
                columnhigh = columnhigh - math.ceil((columnhigh - columnlow)/2)
        for char in sub2:
            if char == 'R':
                rowlow = rowlow + math.ceil((rowhigh - rowlow)/2)
            else:
                rowhigh = rowhigh - math.ceil((rowhigh - rowlow)/2)
        seats.append(columnhigh * 8 + rowhigh)
        if seatID < (columnhigh * 8 + rowhigh):
            seatID = columnhigh * 8 + rowhigh
        columnhigh = 127
        columnlow = 0
        rowhigh = 7
        rowlow = 0

print(seatID)

f.close()

#task2
seats.sort()
for index, seat in enumerate(seats, start=0):
    if seat - seats[index-1] == 2:
        print("+1 seat:"+str(seat)+" -1 seat:"+str(seats[index-1])+" seat:"+str(seat-1))