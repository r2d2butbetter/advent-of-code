
def getinput():
    with open("Day7/input.txt") as inputfile:
        return inputfile.read().strip()

def checksum(res, nums):
    ops = ['+', '*', '||']
    op_combinations = [[]]
    
    for _ in range(len(nums) - 1):
        new_combinations = []
        for comb in op_combinations:
            for op in ops:
                new_combinations.append(comb + [op])
        op_combinations = new_combinations

    def evaluate_expression(expression):
        tokens = expression.split()
        total = tokens[0]
        i = 1
        while i < len(tokens):
            op = tokens[i]
            num = tokens[i + 1]
            if op == '+':
                total = str(int(total) + int(num))
            elif op == '*':
                total = str(int(total) * int(num))
            elif op == '||':
                total += num
            i += 2
        return total

    for op_comb in op_combinations:
        expression = str(nums[0])
        for num, op in zip(nums[1:], op_comb):
            expression += f' {op} {num}'
        if evaluate_expression(expression) == str(res):
            return True
    return False

if __name__ == "__main__":
    inputstr = getinput().splitlines()
    count = 0

    for line in inputstr:
        res, nums = line.split(":")
        res = res.strip()
        nums = list(map(str.strip, nums.split()))

        # print(res, "\n")
        if checksum(res, nums):
            # print(res, "\n")
            count += int(res)
    
    print("Part 1: ", count)