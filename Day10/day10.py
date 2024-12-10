def getinput():
    with open("Day10/input.txt") as inputfile:
        return inputfile.readlines()
    

def get_neighbors(x, y, current_height):
    neighbors = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == current_height + 1:
                neighbors.append((nx, ny))
    return neighbors

if __name__ == "__main__":
    inputstrs=getinput()
    grid = []
    for line in inputstrs:
        grid.append(list(map(int, line.strip())))

    rows = len(grid)
    cols = len(grid[0])

    trailheads=[]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==0:
                trailheads.append((i,j))

    sum=0
    for th in trailheads:
        visited = set()
        stack = [th]
        final_positions = set()
        while stack:
            x, y = stack.pop()
            height = grid[x][y]
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if height == 9:
                final_positions.add((x, y))
            neighbors = get_neighbors(x, y, height)
            stack.extend(neighbors)
        score = len(final_positions)
        # print(f"Trailhead at {th} has a score of {score}")
        sum+=score

    print("Sum of scores: ", sum)
