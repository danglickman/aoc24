import itertools

input = open('input', 'r').read().strip().splitlines()
edge_list = [l.split("-") for l in input]

edges = set()
nodes = set()
for n1, n2 in edge_list:
    nodes.add(n1)
    nodes.add(n2)
    edges.add((n1, n2))
    edges.add((n2, n1))

sum = 0
for n1, n2, n3 in itertools.combinations(nodes, 3):
    if (n1, n2) in edges and (n2, n3) in edges and (n3, n1) in edges:
        if any(n.startswith("t") for n in [n1, n2, n3]):
            sum += 1
print(sum)