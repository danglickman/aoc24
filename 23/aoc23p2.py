import networkx as nx

input = open('input', 'r').read().strip().splitlines()
edges = [tuple(l.split("-")) for l in input]

G = nx.Graph()
G.add_edges_from(edges)

cliques = nx.find_cliques(G)
largest = max(cliques, key=len)
print(",".join(sorted(largest)))