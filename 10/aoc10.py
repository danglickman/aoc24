import itertools
import operator
from functools import reduce

with open('input') as f:
    input = f.read().strip()

input_map = [list(map(int,list(l))) for l in input.splitlines()]

directions = [(-1,0), (0,1),(1,0),(0,-1)]
n_rows = len(input_map)
n_cols = len(input_map[0])

def in_range(pos):
    r,c = pos
    return 0 <= r < n_rows and 0 <= c < n_cols

def count_trails(r, c, f, to):
    if input_map[r][c] != f:
        return []
    elif f==to:
        return [(r,c)]
    else:
        # return itertools.chain.from_iterable(count_trails(r + dr, c + dc, f+1, to) for dr, dc in directions if in_range((r+dr,c+dc)))
        return list(reduce(operator.add,
            [count_trails(r + dr, c + dc, f + 1, to) for dr, dc in directions if in_range((r + dr, c + dc))]))
p1 = 0
p2 = 0
for i in range(n_rows):
    for j in range(n_cols):
        search = count_trails(i, j, 0, 9)
        p2 += len(search)
        p1 += len(set(search))

print(p1)
print(p2)
