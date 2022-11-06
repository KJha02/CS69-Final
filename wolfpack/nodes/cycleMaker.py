# Andrew Chen
# this file contains utility functions for generating a patrol cycle for a particular map file

# d the the width of space in front of a robot that it can detect intruders in
from random import randint

d = .5
# 0 = empty 2d x 2d square
# 1 = occupied 2d x 2d square
map = [
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
]
map = [
  [0,0],
  [0,0],
]

def MakeGrid(map):
  length = len(map)
  width = len(map[0])
  grid = dict()
  for y in range(width):
    for x in range(length):
      if map[x][y] == 0:
        up = y < width - 1
        down = y > 0
        right = x < length - 1
        left = x > 0
        adjacent = []
        if (up):
          adjacent.append((x,y+1))
        if (down):
          adjacent.append((x,y-1))
        if (left):
          adjacent.append((x-1,y))
        if (right):
          adjacent.append((x+1,y))
        grid[(x,y)] = adjacent
  return grid

def Kruskal(grid):
  seen = set()
  frontier = []
  mst = dict()
  first = grid.iterkeys().next()
  frontier.append(first)
  seen.add(first)
  while len(frontier) > 0:
    k = frontier.pop()
    for a in grid[k]:
      if a not in seen:
        seen.add(a)
        if k in mst:
          mst[k].append(a)
        else:
          mst[k] = [a]
        if a in mst:
          mst[a].append(k)
        else:
          mst[a] = [k]
        frontier.append(a)
  return mst


def SmallToBig(x, y):
  new_x = x // 2
  new_y = y // 2
  return (new_x, new_y)

def MakeCycle(mst):
  firstBig = grid.iterkeys().next()
  firstSmall = (firstBig[0] * 2 + randint(0,1), firstBig[1] * 2 + randint(0,1))

  cycle = []
  curr = firstSmall
  while(curr not in cycle):
    cycle.append(curr)
    (x,y) = curr
    isRight = x % 2 == 1
    isBottom = y % 2 == 0
    this_big = SmallToBig(x,y)
    if (not isRight and not isBottom): # top left
      up_big = (this_big[0], this_big[1]+1)

      # try going right, check if the tree is going up
      if (up_big not in mst[this_big]):
        curr = (x+1,y)
      else: # go up if the tree is going up
        curr = (x, y+1)

    elif (isRight and not isBottom): # top right
      right_big = (this_big[0] + 1, this_big[1])

      # try going down, check if the tree is going right
      if (right_big not in mst[this_big]):
        curr = (x,y-1)
      else: # go right if the tree is going right
        curr = (x+1, y)

    elif (isRight and isBottom): # bottom right
      down_big = (this_big[0], this_big[1] - 1)

      # try going left, check if the tree is going down
      if (down_big not in mst[this_big]):
        curr = (x-1,y)
      else: # go down if the tree is going down
        curr = (x, y-1)
    else: # bottom left
      left_big = (this_big[0] - 1, this_big[1])

      # try going up, check if the tree is going left
      if (left_big not in mst[this_big]):
        curr = (x,y+1)
      else: # go left if the tree is going left
        curr = (x-1, y)

  return cycle

grid = MakeGrid(map)
mst = Kruskal(grid)
cycle = MakeCycle(mst)
