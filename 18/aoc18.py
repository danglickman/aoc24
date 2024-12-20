from collections import deque

input = open('input', 'r').read().strip().split('\n')
bytes = [tuple(map(int,l.split(','))) for l in input]

# size = 6
size = 70

# time = 12
time_init = 1024
# bytes_fallen = set(bytes[:time])

start = (0,0)
end = (size,size)

def in_range(pos):
    return 0 <= pos[0] <= size and 0 <= pos[1] <= size
def get_neighbours(pos):
    return [(pos[0]+1,pos[1]), (pos[0]-1,pos[1]), (pos[0],pos[1]+1), (pos[0],pos[1]-1)]

times = []

# binary search for last viable time
time_min = time_init
time_max = size * size
while True:
    if time_min > time_max:
        break
    if len(times)==0:
        time = time_min
    else:
        time = (time_max + time_min) // 2
    bytes_fallen = set(bytes[:time])
    frontier = deque([(start, 0)])
    visited = set()
    found = False
    while frontier:
        pos, steps = frontier.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        if pos == end:
            times.append((time, steps))
            time_min = time + 1
            found = True
            break
        for n in get_neighbours(pos):
            if n not in visited and in_range(n) and not (n in bytes_fallen):
                frontier.append((n, steps+1))
    if not found:
        time_max = time-1

print(times[0][1])
# print(times[-1])
print(bytes[times[-1][0]])