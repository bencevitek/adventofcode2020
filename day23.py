#inputstring = "389125467"
inputstring = "193467258"

currentcup = int(inputstring[0])

def gettarget(num, numbers):
    found = False
    while not found:
        if numbers.find(str(num)) != -1:
            return str(num)
        num -= 1
        if num < 1:
            num = 9

for x in range(100):
    cut = inputstring[1:4]
    inputstring = inputstring.replace(cut, "")
    target = gettarget(currentcup-1,inputstring)
    inputstring = inputstring.replace(target, target+cut)
    inputstring = inputstring[1:] + inputstring[0]
    currentcup = int(inputstring[0])

print(inputstring[inputstring.find("1")+1:] + inputstring[:inputstring.find("1")])

#task2

