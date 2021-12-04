import re
rules = {}
texts = []
with open('day19.txt') as f:
    for line in f:
        if re.search("[0-9]:",line):
            match = re.search("([0-9]+):(.*)",line)
            rules[match[1]] = match[2]
        elif line != '\n':
            texts.append(line)

replacethese = {}
for rule in list(rules.keys()):
    if rules[rule] == " \"a\"":
        replacethese[rule] = "a"
        del rules[rule]
    elif rules[rule] == " \"b\"":
        replacethese[rule] = "b"
        del rules[rule]

changed = True
while changed:
    changed = False
    for rule in list(rules.keys()):
        for reppattern in replacethese:
            rules[rule] = re.sub(" "+reppattern+"$| "+reppattern+" "," "+replacethese[reppattern]+" ",rules[rule])
            if not re.search("[0-9]",rules[rule]):
                replacethese[rule] = "("+rules[rule].replace(" ","")+")"
                del rules[rule]
                changed = True
                break

print(replacethese["42"])
print(replacethese["31"])
counter = 0
for text in texts:
    if re.search("^"+replacethese["0"]+"$",text):
        counter += 1
print(counter)

#task2 not general solution only works because the length of the input is limited
counter = 0
for text in texts:
    if re.search("^"+replacethese["42"]+"+("+replacethese["42"]+"{1}"+replacethese["31"]+"{1}|"+replacethese["42"]+"{2}"+replacethese["31"]+"{2}|"+replacethese["42"]+"{3}"+replacethese["31"]+"{3}|"+replacethese["42"]+"{4}"+replacethese["31"]+"{4})$",text):
        print(text)
        counter += 1
print(counter)