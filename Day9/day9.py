def getinput():
    with open("Day9/input.txt") as inputfile:
        return inputfile.read()

def mapparse(inputstr):
    listofno = []
    blocks = []
    for i in inputstr:
        listofno.append(int(i))

    fid = 0
    i = 0
    isfile = True
    while i < len(listofno):
        length = listofno[i]
        if isfile:
            blocks.extend([fid] * length)
            fid += 1
        else:
            blocks.extend(['.'] * length)
        isfile = not isfile
        i += 1
    return blocks

def compact(blocks):
    while True:
        try:
            lfree = blocks.index('.')
        except ValueError:
            break  # No free space found

        rblock = None
        for i in range(len(blocks)-1, -1, -1):
            if blocks[i] != '.':
                rblock = i
                break
        if rblock is None or rblock <= lfree:
            break

        blocks[lfree], blocks[rblock] = blocks[rblock], '.'

    return blocks

def checksum(blocks):
    total = 0
    for i, block in enumerate(blocks):
        if block != '.':
            total += i * block
    return total

if __name__ == "__main__":
    inputstr = getinput()
    blocks = mapparse(inputstr)
    blocks = compact(blocks)
    checksum = checksum(blocks)
    print(checksum)