def getinput(): 
  with open(f'Day6/input.txt') as inputFile:
    return inputFile.read().strip()
  

def check_limits(dimensions, x, y):
  return 0 <= x < dimensions[0] and 0 <= y < dimensions[1]

def check_loop(x, y, direction, obstacles):
  new_obstacle = (x + direction[0], y + direction[1])
  obstacles.add(new_obstacle) # Add obstacle about to be tested
  visitedset = set() # loop exists, if we visit a location twice with same direction

  while (x, y, direction) not in visitedset:
    visitedset.add((x, y, direction))
    new_x, new_y = x + direction[0], y + direction[1]
    if (new_x, new_y) in obstacles:
      direction = (-direction[1], direction[0]) #right turn
      continue
    if not check_limits(dimensions, new_x, new_y):
      obstacles.remove(new_obstacle)
      return False
    x, y = new_x, new_y

  obstacles.remove(new_obstacle)
  return True

if __name__ == "__main__":
    strinput = getinput().splitlines()
    dimensions = (len(strinput[0]), len(strinput))
    obstacles = set()
    pos_x, pos_y = 0, 0
    for y, line in enumerate(strinput):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((x, y))
            elif char == '^':
                pos_x, pos_y = x, y
    direction = (0, -1) # Up

    visited = {(pos_x, pos_y)}
    new_obstacles = set()
    while True:
    # Calculate next position:
        new_x, new_y = pos_x + direction[0], pos_y + direction[1]
        if not check_limits(dimensions, new_x, new_y):
            break
        
        if (new_x, new_y) in obstacles:
            direction = (-direction[1], direction[0]) # Turn right
            continue

        # Part 2:
        if (new_x, new_y) not in visited and (new_x, new_y) not in new_obstacles:
            if check_loop(pos_x, pos_y, direction, obstacles):
                new_obstacles.add((new_x, new_y))

        # Update position:
        pos_x, pos_y = new_x, new_y
        visited.add((pos_x, pos_y))

    print("Part 1: ", len(visited))
    print("Part 2: ", len(new_obstacles))