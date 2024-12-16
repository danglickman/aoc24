import itertools
import re
import numpy as np

with open('input') as f:
    input = f.read().strip()
input_lines = input.splitlines()
n_robots= len(input_lines)

def parse_ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))

dimensions = np.array([101, 103])
# test
# dimensions = np.array([11, 7])

params = [parse_ints(line) for line in input_lines]

positions = np.array([r[:2] for r in params])
velocities = np.array([r[2:] for r in params])


start = positions
def step(steps=1):
    global positions, velocities
    positions =  (positions +  (velocities * steps))% dimensions

def safety_factor():
    on_left = positions[:, 0] < dimensions[0] // 2
    on_right = positions[:, 0] > dimensions[0] // 2
    on_top = positions[:, 1] < dimensions[1] // 2
    on_bottom = positions[:, 1] > dimensions[1] // 2
    return np.prod([np.sum(h & v) for h, v in itertools.product([on_left, on_right], [on_top, on_bottom])])

step(steps=100)
print(safety_factor())

# 103 * 101= 10403
positions = start
def print_moment(moment):
    positions = moment
    for r in range(dimensions[1]):
        for c in range(dimensions[0]):
            if np.any((positions[:,0] == c) & (positions[:,1] == r)):
                print("#", end="")
            else:
                print(".", end="")
        print()

moments = []
sf = np.zeros(10403)
for i in range(10403):
    step()
    moments.append(positions)
    sf[i] = safety_factor()

print(np.argmin(sf)+1)
print_moment(moments[np.argmin(sf)])
