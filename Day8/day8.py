def getinput(inputfile):
    with open(inputfile) as f:
        return f.read().strip().split('\n')

def collect_positions(grid):
    positions = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != '.':
                if char not in positions:
                    positions[char] = []
                positions[char].append((r, c))
    return positions

def check_alignment(r, c, r1, c1, r2, c2):
    return (r - r1) * (c - c2) == (r - r2) * (c - c1)

def find_aligned_points(grid, positions):
    part1, part2 = set(), set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for k, vs in positions.items():
                for i in range(len(vs)):
                    for j in range(i + 1, len(vs)):
                        r1, c1 = vs[i]
                        r2, c2 = vs[j]
                        d1 = abs(r - r1) + abs(c - c1)
                        d2 = abs(r - r2) + abs(c - c2)
                        if (d1 == 2 * d2 or d1 * 2 == d2) and check_alignment(r, c, r1, c1, r2, c2):
                            part1.add((r, c))
                        if check_alignment(r, c, r1, c1, r2, c2):
                            part2.add((r, c))
    return len(part1), len(part2)


if __name__ == "__main__":
    grid = getinput('Day8/input.txt')
    positions = collect_positions(grid)
    p1, p2 = find_aligned_points(grid, positions)
    print("Part1: ", p1)
    print("Part2: ", p2)
