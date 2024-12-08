import itertools
from collections import defaultdict

with open('input') as f:
    input_lines = f.read().strip().splitlines()

n_rows = len(input_lines)
n_cols = len(input_lines[0])

ant_locs = defaultdict(list)
for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        if char != ".":
            ant_locs[char].append((i, j))

antinodes1 = set()
antinodes2 = set()
def in_range(pos):
    r,c = pos
    return 0 <= r < n_rows and 0 <= c < n_cols

for loc_list in ant_locs.values():
    for (ar, ac), (br, bc) in itertools.permutations(loc_list, 2):
        dr = ar - br
        dc = ac - bc
        antinodes1.add((ar + dr, ac + dc))
        for i in range(max(n_cols,n_rows)):
            antinodes2.add((ar + i*dr, ac + i*dc))

print(sum(map(in_range, antinodes1)))
print(sum(map(in_range, antinodes2)))