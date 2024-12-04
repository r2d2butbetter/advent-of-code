def read_grid(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, down-right, down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, up-left, up-right
    ]
    
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True
    
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1
    return count

if __name__ == "__main__":
    grid = read_grid("Day4/input.txt")
    word = "XMAS"
    count = search_word(grid, word)
    print(f"Total instances of '{word}': {count}")