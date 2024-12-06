import copy
import itertools
import sys
from collections import defaultdict
# Hint: use PyPy


with open('input') as f:
    input_str = f.read()

input_map = [list(l) for l in input_str.splitlines()]


rows = len(input_map)
cols = len(input_map[0])
start = input_str.index('^')
gr,gc = divmod(start,cols+1) # newlines

directions = [(-1,0), (0,1),(1,0),(0,-1), ]

def guard_path(input_map, gr, gc):
    visited = defaultdict(list)
    dir_idx = 0
    visited[(gr, gc)] = [dir_idx]
    while True:
        dr, dc = directions[dir_idx]
        while (0 <= gr+dr < rows and 0 <= gc+dc < cols) and input_map[gr+dr][gc+dc] == '#':
            dir_idx = (dir_idx + 1) % 4
            dr, dc = directions[dir_idx]
            visited[(gr, gc)].append(dir_idx)
            if len(visited[(gr, gc)]) == 4: return None

        gr += dr
        gc += dc
        if not (0 <= gr < rows and 0 <= gc < cols):
            break
        if visited[(gr,gc)] and dir_idx in visited[(gr,gc)]:
            return None
        visited[(gr,gc)].append(dir_idx)
    return visited

visited = guard_path(input_map, gr, gc)
print(sum(visited[(r,c)]!=[] for r, c in itertools.product(range(rows), range(cols))))

# part 2
result = 0
for i, row in enumerate(input_map):
    for j, el in enumerate(row):
        if el != '#' and el != '^':
            new_place = copy.deepcopy(input_map)
            new_place[i][j] = '#'
            if guard_path(new_place, gr,gc) is None:
                result += 1

print(result)



