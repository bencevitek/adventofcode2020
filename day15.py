secondlastoccurence = {}
lastoccurence = {}
input = [8,13,1,0,18,9]
for index, imp in enumerate(input, start=1):
    secondlastoccurence[imp] = index

prevnumber = 9

def calculate(lastround, prevnumber):
    for x in range(7, lastround):
        #print(prevnumber, x)
        if prevnumber in lastoccurence:
            diff = lastoccurence[prevnumber] - secondlastoccurence[prevnumber]
            if diff in secondlastoccurence:
                if diff in lastoccurence:
                    secondlastoccurence[diff] = lastoccurence[diff]
                    lastoccurence[diff] = x
                else:
                    lastoccurence[diff] = x
            else:
                secondlastoccurence[diff] = x
            prevnumber = diff
        else:
            if 0 in secondlastoccurence:
                if 0 in lastoccurence:
                    secondlastoccurence[0] = lastoccurence[0]
                    lastoccurence[0] = x
                else:
                    lastoccurence[0] = x
            else:
                secondlastoccurence[0] = x
            prevnumber = 0
    print(prevnumber)

calculate(2021, prevnumber)
secondlastoccurence = {}
lastoccurence = {}
input = [8,13,1,0,18,9]
for index, imp in enumerate(input, start=1):
    secondlastoccurence[imp] = index
calculate(30000001, prevnumber)