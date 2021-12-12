
p1 = []
p2 = []
currplayer = ""
with open('day22.txt') as f:
    for line in f:
        if line.strip() == "Player 1:":
            currplayer = "Player1"
        elif line.strip() == "Player 2:":
            currplayer = "Player2"
        elif line != '\n':
            if currplayer == "Player1":
                p1.append(int(line))
            else:
                p2.append(int(line))

p1task2 = p1.copy()
p2task2 = p2.copy()

while len(p1) != 0 and len(p2) != 0:
    if p1[0] > p2[0]:
        p1.append(p1[0])
        p1.append(p2[0])
    else:
        p2.append(p2[0])
        p2.append(p1[0])
    p1.pop(0)
    p2.pop(0)

def calculatefinal(deck):
    summ = 0
    for i in range(len(deck)) :
        summ += deck[i] * (len(deck)-i)
    return summ

if len(p1) > 0:
    print(calculatefinal(p1))
else:
    print(calculatefinal(p2))


#task2
def playgame(deck1, deck2):
    olddecks1 = []
    olddecks2 = []
    while len(deck1) != 0 and len(deck2) != 0:
        if deck1 in olddecks1 and deck2 in olddecks2:
            result = []
            result.append("p1")
            result.append(deck1)
            return result
        else:
            olddecks1.append(deck1.copy())
            olddecks2.append(deck2.copy())
            p1first = deck1.pop(0)
            p2first = deck2.pop(0)
            if p1first <= len(deck1) and p2first <= len(deck2):
                res = playgame(deck1[:p1first], deck2[:p2first])
                if res[0] == "p1":
                    deck1.append(p1first)
                    deck1.append(p2first)
                else:
                    deck2.append(p2first)
                    deck2.append(p1first)
            else:
                if p1first > p2first:
                    deck1.append(p1first)
                    deck1.append(p2first)
                else:
                    deck2.append(p2first)
                    deck2.append(p1first)
    result = []
    if len(deck1) > 0:
        result.append("p1")
        result.append(deck1)
        return result
    else:
        result.append("p2")
        result.append(deck2)
        return result

print(calculatefinal(playgame(p1task2, p2task2)[1]))