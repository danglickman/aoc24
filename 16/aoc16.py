import heapq
from collections import deque

input = open('input', 'r').read().strip()

input_map = [list(l) for l in input.splitlines()]
directions = [(-1,0), (0,1),(1,0),(0,-1)]
n_rows = len(input_map)
n_cols = len(input_map[0])

# find start and end:
for i, l in enumerate(input_map):
    for j, c in enumerate(l):
        if c == 'S':
            start = ((i,j), 1)
        elif c == 'E':
            end = (i,j)

# could learn networkx but let's practice Dijkstra's
# state of form row, col, orientation
# transitions of move ahead one (cost 1) , turn c/cc (cost 1000)
visited = {}
frontier = [(0, start)]
min_cost = None
while frontier:
    curr = heapq.heappop(frontier)
    cost, pos = curr
    if pos in visited:
        continue
    if min_cost is not None and cost > min_cost:
        continue
    visited[pos] = cost
    if pos[0] == end:
        if min_cost is None or cost < min_cost:
            min_cost = cost
        continue

    r, c = pos[0]
    dr, dc = directions[pos[1]]
    if input_map[r+dr][c+dc] != '#':
        if ((r+dr, c+dc),dir) not in visited:
            heapq.heappush(frontier, (cost+1, ((r+dr, c+dc), pos[1])))
    if min_cost is not None and cost + 1000 > min_cost:
        continue
    if ((r, c), (pos[1]+1)%4) not in visited:
        heapq.heappush(frontier, (cost+1000, ((r, c), (pos[1]+1)%4)))
    if ((r, c), (pos[1]-1)%4) not in visited:
        heapq.heappush(frontier, (cost+1000, ((r, c), (pos[1]-1)%4)))

all_states = set()
for pos in [(end, dir) for dir in range(4)]:
    to_recover = deque()
    if pos in visited:
        to_recover.append(pos)
    else:
        continue
    while to_recover:
        curr = to_recover.popleft()
        all_states.add(curr[0])
        r, c = curr[0]
        dx = curr[1]
        dr, dc = directions[dx]
        prev = ((r-dr, c-dc), dx)
        cost = visited[curr]
        if prev in visited:
            if visited[prev] == cost - 1:
                to_recover.append(prev)
        prev = ((r, c), (dx + 1) % 4)
        if prev in visited and visited[prev] == cost - 1000:
            to_recover.append(prev)
        prev = ((r, c), (dx - 1) % 4)
        if prev in visited and visited[prev] == cost - 1000:
            to_recover.append(prev)

print(min_cost)
print(len(all_states))

# for i in range(n_rows):
#     for j in range(n_cols):
#         if (i, j) in all_states:
#             print("O", end="")
#         else:
#             print(input_map[i][j], end="")
#     print()
