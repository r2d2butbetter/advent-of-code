import re

if __name__ == "__main__":
    with open("Day3/input.txt", "r") as data:
        content = data.read()
        
        pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        matches = pattern.findall(content)
        
        total_sum = sum(int(x) * int(y) for x, y in matches)
        
        print(total_sum)