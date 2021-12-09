import re
ingredients = []
allergens = {}
linecounter = 0
with open('day21.txt') as f:
    for line in f:
        ingredients.append(re.search("([ a-z]+) \(",line)[1])
        aller = re.search("contains ([ ,a-z]+)",line)[1].split(", ")
        for a in aller:
            if a in allergens:
                allergens[a].append(linecounter)
            else:
                allergens[a] = []
                allergens[a].append(linecounter)
        linecounter += 1

def removepoison(poison):
    for index in range(0,len(ingredients)):
        ingredients[index] = re.sub(" "+poison+"$|^"+poison+" ","",ingredients[index])
        ingredients[index] = re.sub(" "+poison+" "," ",ingredients[index])

listofpoisonousevilthings = {}
finished = False
while not finished:
    finished = True
    for allergen in allergens:
        base = allergens[allergen][0]
        count = 0
        poison = ""
        for a in ingredients[base].split(" "):
            contains = True
            for ingline in allergens[allergen][1:]:
                if not re.search(a, ingredients[ingline]):
                    contains = False
            if contains:
                poison = a
                count += 1
        if count == 1:
            removepoison(poison)
            listofpoisonousevilthings[allergen] = poison
            finished = False

summ = 0
for ing in ingredients:
    summ += len(ing.split(" "))
print(summ)
print(",".join(dict(sorted(listofpoisonousevilthings.items())).values()))