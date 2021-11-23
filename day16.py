import re
lowest = 100
highest = 0
tickets = []
valuedict = {}
with open('day16.txt') as f:
    for line in f:
        if re.search("[a-z ]: [0-9]+.*", line):
            match = re.search("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", line)
            if int(match[2]) < lowest:
                lowest = int(match[2])
            if int(match[5]) > highest:
                highest = int(match[5])
            valuedict[match[1]] = [int(match[2]), int(match[3]), int(match[4]), int(match[5])]
        if re.search("^[0-9].*", line):
            tickets.append(line)
sum = 0
separatedvalues = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: []}
valid = True
for ticket in tickets[:]:
    ticketvalues = ticket.split(",")
    for val in ticketvalues:
        if int(val) < lowest or int(val) > highest:
            sum += int(val)
            tickets.remove(ticket)
            valid = False
    if valid:
        for index, tic in enumerate(ticketvalues, start=1):
            separatedvalues[index].append(int(tic))
    else:
        valid = True

print(sum)

final = 1
foundall = False
while not foundall:
    for a in valuedict:
        found = 0
        for b in separatedvalues:
            fullok = True
            for c in separatedvalues[b]:
                if not (valuedict[a][0] <= c <= valuedict[a][1]) and not (valuedict[a][2] <= c <= valuedict[a][3]):
                    fullok = False
                    break
            if fullok:
                if found == 0:
                    found = b
                else:
                    found = 0
                    break
                #break
        if found != 0:
            if re.search("^departure.*", a):
                    final *= separatedvalues[found][0]
            del separatedvalues[found]
            if len(separatedvalues) == 0:
                foundall = True

print(final)