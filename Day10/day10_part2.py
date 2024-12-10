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

def pathcount(x, y, memo):
    if (x, y) in memo:
        return memo[(x, y)]
    height = grid[x][y]
    if height == 9:
        memo[(x, y)] = 1
        return 1
    total_paths = 0
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == height + 1:
                total_paths += pathcount(nx, ny, memo)
    memo[(x, y)] = total_paths
    return total_paths

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
        memo = {}
        rating = pathcount(th[0], th[1], memo)
        # print(f"Trailhead at {th} has a rating of {rating}")
        sum+=rating

    print("Sum of scores: ", sum)







