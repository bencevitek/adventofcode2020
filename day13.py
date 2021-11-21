#task1
with open('day13.txt') as f:
    time = int(f.readline())
    buses = f.readline().split(",")

buses = [int(bus) for bus in buses if bus != "x"]

smallest = time
sbus = 0
for bus in buses:
    if (int(time/bus)+1)*bus - time < smallest:
        smallest = (int(time/bus)+1)*bus - time
        sbus = bus

print(sbus * smallest)

#task2
with open('day13.txt') as f:
    f.readline()
    buses = f.readline().split(",")
    
busesd = {}
counter = 1
for bus in buses[1:]:
    if bus != "x":
        busesd[int(bus)] = counter
    counter += 1

firstbus = int(buses[0])
target = firstbus
step = firstbus
for bus in busesd:
    while (target + busesd[bus]) % bus != 0:
        target += step
    step *= bus
    
print(target)