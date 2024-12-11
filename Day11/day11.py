import sys
from functools import lru_cache

def getinput():
    with open('Day11/input.txt', 'r') as f:
        return list(map(int, f.read().split()))

@lru_cache (maxsize=None)
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count_stones(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        digits = str(stone)
        half = len(digits) // 2
        left = int(digits[:half].lstrip('0') or '0')
        right = int(digits[half:].lstrip('0') or '0')
        return count_stones(left, blinks - 1) + count_stones(right, blinks - 1)
    else:
        return count_stones(stone * 2024, blinks - 1)
     

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    stones = getinput()
    blinks = int(input("Enter blinks: "))
    total = sum(count_stones(stone, blinks) for stone in stones)
    print(total)