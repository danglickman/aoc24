with open("input") as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [[e for e in l.split()] for l in lines]

l1 = [int(l[0]) for l in lines]
l2 = [int(l[1]) for l in lines]

# part 1
print(sum(abs(a-b) for a,b in zip(sorted(l1), sorted(l2))))

# part 2
vals = dict.fromkeys(l1, 0)
for v in l2:
    if v in vals:
        vals[v] += 1
result = 0
for k, v in vals.items():
    result += k*v
print(result)