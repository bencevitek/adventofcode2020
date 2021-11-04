#task1
group = ''
unique = ''
counter = 0
with open('day6.txt') as f:
    for line in f:
        group = group + line.rstrip()
        if line in ['\n', '\r\n']:
            #group = ''.join(set(group))
            for char in group:
                if char not in unique:
                    unique = unique + char
            #print(unique)
            counter += len(unique)
            group = ''
            unique = ''

print(counter)
f.close()

#task2
group = ''
groupsize = 0
unique = ''
counter = 0
with open('day6.txt') as f:
    for line in f:
        if line in ['\n', '\r\n']:
            #print(group)
            for char in group:
                if group.count(char) == groupsize and char not in unique:
                    unique = unique + char
            counter += len(unique)
            group = ''
            unique = ''
            groupsize = 0
        else:
            group = group + line.rstrip()
            groupsize += 1

print(counter)
f.close()