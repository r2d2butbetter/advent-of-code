def getinput():
    with open(f"Day6/input.txt", "r") as inputfile:
        return inputfile.read().strip()

def count_steps(grid):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    rows = grid.split('\n')
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            if cell in directions:
                x, y = i, j
                direction = cell
                break
    
    visited = set()
    steps = 0
    while 0 <= x < len(rows) and 0 <= y < len(rows[0]):
        visited.add((x, y))
        dx, dy = directions[direction]
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(rows) and 0 <= new_y < len(rows[0]) and rows[new_x][new_y] == '#':
            direction = turn_right[direction]
        else:
            x, y = new_x, new_y
        steps += 1
    
    return len(visited)

if __name__ == "__main__":
    grid = getinput()
    steps = count_steps(grid)
    print(f"Number of steps: {steps}")
