import functools
from collections import deque, Counter

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

explored = {}
def best_path1(start, end):
    frontier = deque([(0, start)])
    while frontier:
        cost, pos = frontier.popleft()
        if pos == end:
            return cost
        explored[pos] = cost
        for dr, dc in directions:
            new_pos = pos[0] + dr, pos[1] + dc
            if (in_range(new_pos) and
                    input_map[new_pos[0]][new_pos[1]] != '#' and
                    new_pos not in explored):
                frontier.append((cost + 1, new_pos))



@functools.lru_cache(maxsize=None)
def best_path(start, end):
    frontier = deque([(0, start)])
    explored = {}
    while frontier:
        cost, pos = frontier.popleft()
        if pos == end:
            return cost
        explored[pos] = cost
        for dr, dc in directions:
            new_pos = pos[0] + dr, pos[1] + dc
            if (in_range(new_pos) and
                    input_map[new_pos[0]][new_pos[1]] != '#' and
                    new_pos not in explored):
                frontier.append((cost + 1, new_pos))


best_cost = best_path1(start, end)

def cheat_path(start, cheat_len):
    cheats = set()
    for dr, dc in [(1,1), (-1,1), (-1,-1), (1,-1)]:
        for i in range(0, cheat_len+1):
            for j in range(0, cheat_len+1):
                if i+j <= cheat_len:
                    cheat_end = start[0] + dr*i, start[1] + dc*j
                    if in_range(cheat_end) and input_map[cheat_end[0]][cheat_end[1]] != '#':
                        cheats.add((cheat_end, i+j))
    return cheats


good_cheats = {}
for pos, cost in explored.items():
    for cheat_to, cheat_cost in cheat_path(pos, 20):
        cost_rest = best_path(cheat_to, end)
        if cost_rest is None:
            continue
        total_cost = cost + cost_rest + cheat_cost
        if best_cost - total_cost >= 100:
            if (pos, cheat_to) in good_cheats:
                total_cost = min(total_cost, good_cheats[(pos, cheat_to)])
            good_cheats[(pos, cheat_to)] =  total_cost



# c = Counter(best_cost - cost for _,cost in good_cheats.items())
# print(c)
print(len(good_cheats))