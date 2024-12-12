import functools
import itertools
from collections import deque

from nltk.sem.chat80 import borders

with open('input') as f:
    input = f.read().strip()


input_map = [list(l) for l in input.splitlines()]
directions = [(-1,0), (0,1),(1,0),(0,-1)]
n_rows = len(input_map)
n_cols = len(input_map[0])
def in_range(pos):
    r,c = pos
    return 0 <= r < n_rows and 0 <= c < n_cols

regions = []
plot_info = {}

def explore_region(pos):
    # print("exploring from:", pos)
    r,c = pos
    type = input_map[r][c]
    plot_list = []
    region_id = len(regions)
    frontier = deque()
    frontier.append(pos)
    plot_list.append(pos)
    perim_len = 0
    borders = []

    while frontier:
        r, c = frontier.popleft()
        for dr, dc in directions:
            new_pos = r+dr, c+dc
            if (in_range(new_pos) and
                    input_map[new_pos[0]][new_pos[1]] == type):
                if new_pos not in plot_list:
                    plot_list.append(new_pos)
                    frontier.append(new_pos)
                    plot_info[new_pos]=(region_id, type)
            else:
                borders.append(((r,c), new_pos))
                perim_len += 1
    area = len(plot_list)
    regions.append((type, area, perim_len, plot_list, borders))
    return (perim_len, area)


p1 = 0
for i, l in enumerate(input_map):
    for j, plot in enumerate(l):
        if (i, j) in plot_info:
            continue
        perim_len, area = explore_region((i,j))
        p1 += perim_len * area

print(p1)


# part 2
def side_length(border, borders):
    assert(border in borders)
    side_list = []
    dr = border[1][0] - border[0][0]
    dc = border[1][1] - border[0][1]
    if dr == 0:
        bdr = 1
        bdc = 0
    else:
        bdr = 0
        bdc = 1

    length = 1

    first = (border[0][0] + bdr, border[0][1] + bdc)
    second = (border[1][0] + bdr, border[1][1] + bdc)
    while True:
        if (first, second) in borders:
            length += 1
            side_list.append((first, second))
        else:
            break
        first = (first[0] + bdr, first[1] + bdc)
        second = (second[0] + bdr, second[1] + bdc)


    first = (border[0][0] - bdr, border[0][1] - bdc)
    second = (border[1][0] - bdr, border[1][1] - bdc)
    while True:
        if (first, second) in borders:
            length += 1
            side_list.append((first, second))
        else:
            break
        first = (first[0] - bdr, first[1] - bdc)
        second = (second[0] - bdr, second[1] - bdc)

    return length,side_list

p2 = 0
for region in regions:
    # print("analyzing borders in region " , regions.index(region))
    sides = 0
    examined = []
    for border in region[-1]:
        if border in examined:
            continue
        length,side_list = side_length(border, region[-1])
        examined += side_list
        if length != 0:
            sides += 1
    p2 += sides * region[1]

print(p2)