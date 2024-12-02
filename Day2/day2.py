def is_safe(nums):
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        differences = [int(nums[i+1]) - int(nums[i]) for i in range(len(nums)-1)]
        if all(1 <= abs(diff) <= 3 for diff in differences):
            return True
    return False

if __name__=="__main__":
    list1 = []
    list2 = []
    nums=[]
    count_part1 = 0
    count_part2 = 0
    
    with open('Day2/input.txt', 'r') as file:
        for line in file:
            nums = list(map(int, line.split()))
            
            if is_safe(nums):
                count_part1 += 1
                count_part2 += 1
            else:
                # Check if removing one level makes it safe
                for i in range(len(nums)):
                    if is_safe(nums[:i] + nums[i+1:]):
                        count_part2 += 1
                        break
        
        print("Part1: ", count_part1)
        print("Part2: ", count_part2)


