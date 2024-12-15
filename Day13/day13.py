import re
def getinput():
  with open("Day13/input.txt") as inputfile:
    return inputfile.read().strip()

def findWinningCost(x_a, y_a, x_b, y_b, x_p, y_p):
  a = (y_b*x_p - x_b*y_p)/(x_a*y_b - x_b*y_a)
  b = (-y_a*x_p + x_a*y_p)/(x_a*y_b - x_b*y_a)
  if a.is_integer() and b.is_integer():
    return int(3*a + b)
  return 0

part1 = 0
part2 = 0
pattern = re.compile(r"X[=|+]?(\d+), Y[=|+]?(\d+)")
for machine in getinput().split("\n\n"):
  a, b, prize = map(lambda t: (int(t[0]), int(t[1])), pattern.findall(machine)) # don't forget to map tuples of string-matches to tuples of integers
  part1 += findWinningCost(*a, *b, *prize)
  part2 += findWinningCost(*a, *b, prize[0]+10000000000000, prize[1]+10000000000000)

print("Part 1: ", part1)
print("Part 2: ", part2)