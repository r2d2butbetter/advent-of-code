import re

if __name__ == "__main__":
    with open("Day3/input.txt", "r") as data:
        content = data.read()
        
        pattern = re.compile(r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))')
        matches = pattern.findall(content)
        
        enabled = True
        total_sum = 0
        
        for match in matches:
            if match[0] == 'do()':
                enabled = True
            elif match[0] == "don't()":
                enabled = False
            elif enabled:
                x, y = match[1], match[2]
                total_sum += int(x) * int(y)
        
        print(total_sum)