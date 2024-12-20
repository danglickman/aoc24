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
            start = (i,j)
        elif c == 'E':
            end = (i,j)

def in_range(pos):
    r,c = pos
    return 0 <= r < n_rows and 0 <= c < n_cols

def distances_from(target):
    explored = {}
    frontier = deque([(0, target)])
    while frontier:
        cost, pos = frontier.popleft()
        explored[pos] = cost
        for dr, dc in directions:
            new_pos = pos[0] + dr, pos[1] + dc
            if (#in_range(new_pos) and
                    input_map[new_pos[0]][new_pos[1]] != '#' and
                    new_pos not in explored):
                frontier.append((cost + 1, new_pos))
    return explored

cost_to_end = distances_from(end)
cost_to_start = distances_from(start)

base_cost = cost_to_end[start]

cheats = set()
cheat_time = 20
for s in cost_to_start:
    for i in range(0, cheat_time+1):
        for j in range(0, cheat_time+1 - i):
            for dr, dc in [(1,1), (-1,1), (-1,-1), (1,-1)]:
                cheat_end = (s[0] + dr*i, s[1] + dc*j)
                if in_range(cheat_end) and input_map[cheat_end[0]][cheat_end[1]] != '#':
                    total_cost = cost_to_end[cheat_end] + cost_to_start[s] + i + j
                    if base_cost - total_cost >= 100:
                        cheats.add((s, cheat_end))

print(len(cheats))
