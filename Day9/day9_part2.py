def part2f(blocks):
    blocks = blocks.copy()  # blocks gets modified, so it's best to copy it first
    i = 0
    j = len(blocks) - 1
    vacant = [0] * len(blocks)
    while i < j:
        # yield 0 if slot once held a file, but it has been removed:
        for _ in range(vacant[i]):
            yield 0
        # yield id of file that has always been here:
        for _ in range(blocks[i]):
            yield i // 2
        i += 1
        # Try to fill empty slot:
        for candidate in range(j, i, -2):
            if 0 < blocks[candidate] <= blocks[i]:  # 0 == blocks[candidate] would mean that the candidate has already been moved
                # yield id of candidate if it fits in empty slot:
                for _ in range(blocks[candidate]):
                    yield candidate // 2
                blocks[i] -= blocks[candidate]  # reduce empty slot size by candidate size
                vacant[candidate] = blocks[candidate]  # remember to yield 0s instead of candidate id for the candidate later
                blocks[candidate] = 0  # mark candidate as moved
        # yield remaining empty slots:
        for _ in range(blocks[i]):
            yield 0
        i += 1
    # yield remaining ids at the end of the blocks:
    for _ in range(blocks[i]):
        yield i // 2

def getinput():
    with open("Day9/input.txt") as inputfile:
        return inputfile.read()

if __name__ == "__main__":
    inputstr = getinput()
    listofno = []
    blocks = []
    for i in inputstr:
        listofno.append(int(i))

    part2_result = sum(i * id for i, id in enumerate(part2f(listofno)))
    print("Part 2: ", part2_result)