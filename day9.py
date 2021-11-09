numbers = []
with open('day9.txt') as f:
    for line in f:
        numbers.append(int(line))

#task1
def check(first):
    end = first + 24
    target = first + 25
    for i in range(first, end):
        for y in range(i+1,end+1):
            if numbers[i] + numbers[y] == numbers[target]:
                return 0
    return numbers[target]

#task2
def check2(target):
    small = target
    large = 0
    current = 0
    summ = 0
    while current < 1000:
        for num in numbers[current:]:
            summ += num
            if num < small:
                small = num
            if num > large:
                large = num
            if summ > target:
                current += 1
                break
            if summ == target:
                print(large + small)
                return 0
        summ = 0
        small = target
        large = 0


counter = 0
for number in numbers:
    curr = check(counter)
    if curr != 0:
        print(curr)
        check2(curr)
        break
    counter += 1

#22477624
#2980044