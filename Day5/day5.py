def getinput(): 
  with open(f'Day5/input1.txt') as inputFile:
    return inputFile.read().strip()

part1 = 0
part2 = 0

rules_list, updates_list = getinput().split("\n\n")
rules = {}
for rule in rules_list.splitlines():
  left, right = rule.split("|")
  rules.setdefault(left, []).append(right)

update_lines=updates_list.splitlines()
for update in update_lines:
  update = update.split(",")
  oldpages = set()
  valid = True
  for page in update:
    if page not in rules or all([futurepage not in oldpages for futurepage in rules[page]]):
      oldpages.add(page)
    else:
      valid = False
      break
  if valid:
    part1 += int(update[len(update)//2])
  else:
    new_update = [0]*len(update)
    for i in range(len(update)-1, -1, -1): #frm right to left
      for elem in update:
        if elem not in rules or all([futurepage not in update for futurepage in rules[elem]]):
          new_update[i] = elem
          update.remove(elem)
          break
    part2 += int(new_update[len(new_update)//2])

print("Part 1: ", part1)
print("Part 2: ", part2)