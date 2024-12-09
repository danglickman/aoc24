import itertools
from collections import defaultdict
import functools
from collections import defaultdict
from collections import deque


with open('input') as f:
    input = f.read().strip()

seq = list(map(int, list(input)))
total_size = sum(seq)
avail = deque()
files = deque()
disk = []
loc = 0
for i in range(0, len(seq)):
    if i%2==0:
        files.append((loc, seq[i], i//2))
        loc += seq[i]
    else:
        avail.append((loc, seq[i]))
        loc += seq[i]

files2 = files.copy()
avail2 = avail.copy()
disk.append(files.popleft())
# def disk_str():
#     result_str = ""
#     for start, size, id in disk:
#         for _ in range(size):
#             result_str += str(id)
#     print(result_str)
#


while files:
    eloc, esize = avail.popleft()
    # while esize ==0:
    #     disk.append(files.popleft())
    #     eloc, esize = avail.popleft()

    floc, fsize, fid = files.pop()
    ploc, psize, pid = disk[-1]
    if fsize < esize:
        disk.append((ploc+psize, fsize, fid))
        eloc += fsize
        esize -= fsize
        avail.appendleft((eloc, esize))
    elif fsize == esize:
        disk.append((ploc + psize, fsize, fid))
        disk.append(files.popleft())
    else:
        if esize!=0:
            disk.append((ploc+psize, esize, fid))
        fsize -= esize
        files.append((floc, fsize, fid))
        disk.append(files.popleft())

result = sum(sum(id * block for block in range(start, start+size)) for start, size, id in disk)

print(result)


avail = [a for a in avail2 if a[1]!=0]

#pt 2
files = list(files2)
files.reverse()
files_final = []

for floc, fsize, fid in files:
    for i, (eloc, esize) in enumerate(avail):
        if floc <= eloc:
            break
        if fsize < esize:
            floc = eloc
            avail[i] = (eloc+fsize, esize-fsize)
            break
        elif fsize == esize:
            floc = eloc
            del avail[i]
    files_final.append((floc, fsize, fid))

# result = sum(id * size*(start + start + size)//2 for start, size, id in files_final)
result = sum(sum(id * block for block in range(start, start+size)) for start, size, id in files_final)

print(result)