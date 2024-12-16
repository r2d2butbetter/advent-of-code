import sys
import re
import heapq
from collections import deque

sys.setrecursionlimit(10**6)
directions = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

def getinput():
    with open('Day16/input.txt') as inputfile:
        return inputfile.read().strip()

ans = 0
D = getinput()

G = D.split('\n')
R = len(G)
C = len(G[0])
G = []
for row in D.split('\n'):
    G.append(list(row))

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr,sc = r,c
        if G[r][c] == 'E':
            er,ec = r,c

Q = []
SEEN = set()
heapq.heappush(Q, (0,sr,sc,1))
DIST = {}
best = None
while Q:
    d,r,c,dir = heapq.heappop(Q)
    if (r,c,dir) not in DIST:
        DIST[(r,c,dir)] = d
    if r==er and c==ec and best is None:
        best = d
    if (r,c,dir) in SEEN:
        continue
    SEEN.add((r,c,dir))
    dr,dc = directions[dir]
    rr,cc = r+dr,c+dc
    if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
        heapq.heappush(Q, (d+1, rr,cc,dir))
    heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
    heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))
print("Part 1: ", best)

Q = []
SEEN = set()
for dir in range(4):
    heapq.heappush(Q, (0,er,ec,dir))
DIST2 = {}
while Q:
    d,r,c,dir = heapq.heappop(Q)
    if (r,c,dir) not in DIST2:
        DIST2[(r,c,dir)] = d
    if (r,c,dir) in SEEN:
        continue
    SEEN.add((r,c,dir))
    # going backwards instead of forwards here
    dr,dc = directions[(dir+2)%4]
    rr,cc = r+dr,c+dc
    if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
        heapq.heappush(Q, (d+1, rr,cc,dir))
    heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
    heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))

count_squares = set()
for r in range(R):
    for c in range(C):
        for dir in range(4):
            if (r,c,dir) in DIST and (r,c,dir) in DIST2 and DIST[(r,c,dir)] + DIST2[(r,c,dir)] == best:
                count_squares.add((r,c))
print("Part 2: ", len(count_squares))