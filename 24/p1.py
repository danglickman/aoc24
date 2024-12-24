import functools

input = open('input', 'r').read().strip()
a, b = input.split('\n\n')
#
comps = {}
for l in a.split('\n'):
    wire, val = l.split(': ')
    comps[wire] = int(val)

for l in b.split('\n'):
    inst, target = l.split(' -> ')
    w1, op, w2 = inst.split()
    comps[target] = inst

@functools.cache
def compute(wire):
    recipe = comps[wire]
    if isinstance(recipe, int):
        return recipe
    else:
        w1, op, w2 = recipe.split()
        w1 = compute(w1)
        w2 = compute(w2)
        match op:
            case "AND":
                return w1 & w2
            case "OR":
                return w1 | w2
            case "XOR":
                return w1 ^ w2

final_vals = {}
for wire in comps:
    final_vals[wire] = compute(wire)\

binary = "".join([str(val) for wire, val in reversed(sorted(final_vals.items())) if wire.startswith('z')])
res = int(binary, 2)
print(res)