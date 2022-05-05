import logging

logging.basicConfig(level=logging.INFO)

doorpub = 9232416
cardpub = 14144084

def getloop(key):
    curr = 1
    loopnum = 0
    while curr != key:
        curr = curr * 7 % 20201227
        loopnum += 1
    logging.debug(f"loopnum: {loopnum}")
    return loopnum

def encrytion(pkey, loop):
    encrypted = 1
    for x in range(loop):
        encrypted = encrypted * pkey % 20201227
    return encrypted

logging.info(f"Loop: {encrytion(cardpub, getloop(doorpub))}")