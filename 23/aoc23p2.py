import networkx as nx

input = open('input', 'r').read().strip().splitlines()
edge_list = [l.split("-") for l in input]

edges = set()
nodes = set()
for n1, n2 in edge_list:
    nodes.add(n1)
    nodes.add(n2)
    edges.add((n1, n2))
    edges.add((n2, n1))


G = nx.Graph()
G.add_edges_from(edges)

cliques = nx.find_cliques(G)
largest = max(cliques, key=len)
print(",".join(sorted(largest)))