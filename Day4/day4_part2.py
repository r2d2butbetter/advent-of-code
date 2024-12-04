def find_xmas(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (grid[i-1][j-1] == 'M' and grid[i-1][j+1] == 'S' and
                grid[i][j] == 'A' and
                grid[i+1][j-1] == 'M' and grid[i+1][j+1] == 'S'):
                count += 1

            if (grid[i-1][j-1] == 'S' and grid[i-1][j+1] == 'M' and
                grid[i][j] == 'A' and
                grid[i+1][j-1] == 'S' and grid[i+1][j+1] == 'M'):
                count += 1

            if (grid[i-1][j-1] == 'M' and grid[i-1][j+1] == 'M' and
                grid[i][j] == 'A' and
                grid[i+1][j-1] == 'S' and grid[i+1][j+1] == 'S'):
                count += 1

            if (grid[i-1][j-1] == 'S' and grid[i-1][j+1] == 'S' and
                grid[i][j] == 'A' and
                grid[i+1][j-1] == 'M' and grid[i+1][j+1] == 'M'):
                count += 1
    
    return count

def readfromfile(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

if __name__ == "__main__":
    grid = readfromfile('Day4/input.txt')
    print(find_xmas(grid))