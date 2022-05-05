import logging

logging.basicConfig(level=logging.INFO)

flipped = {}
with open('day24.txt') as f:
    for route in f:
        x = 0
        y = 0
        direction = ""
        for char in route:
            if char in "ew":
                direction += char
                logging.debug(f"Current direction: {direction}")
                if direction == "nw":
                    x += 1
                elif direction == "w":
                    y += 1
                elif direction == "sw":
                    x -= 1
                    y += 1
                elif direction == "se":
                    x -= 1
                elif direction == "e":
                    y -= 1
                else:
                    x += 1
                    y -= 1
                direction = ""
                logging.debug(f"current cordinates: {x} and {y}")
            else:
                direction = char
        logging.debug(f"Final cordinates: {x} and {y}")
        if (x, y) in flipped:
            del flipped[(x, y)]
        else:
            flipped[(x, y)] = "black"

print(len(flipped))