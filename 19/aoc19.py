import functools

input = open('input', 'r').read().strip()

towels, onsens= input.split('\n\n')

towels = [t.strip() for t in towels.split(',')]
onsens = onsens.splitlines()
# print(towels)
# print(onsens)

@functools.lru_cache(maxsize=None)
def makable(o):
    if len(o) == 0:
        return True
    for t in towels:
        if len(o) < len(t):
            continue
        else:
            if o.startswith(t):
                if makable(o[len(t):]):
                    return True
    return False

p1 = 0
for o in onsens:
    if makable(o):
        p1+=1
        # print(o)

print(p1)