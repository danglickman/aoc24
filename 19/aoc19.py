import functools

input = open('input', 'r').read().strip()

towels, onsens= input.split('\n\n')

towels = [t.strip() for t in towels.split(',')]
onsens = onsens.splitlines()

@functools.lru_cache(maxsize=None)
def makable(o):
    res = 0
    if len(o) == 0:
        return 1
    for t in towels:
        if o.startswith(t):
            if n :=makable(o[len(t):]):
                res +=n
    return res

p1 = 0
p2 = 0
for o in onsens:
    if n :=makable(o):
        p1+=1
        p2 += n
        # print(o)

print(p1)
print(p2)