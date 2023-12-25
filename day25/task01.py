from math import prod
import networkx

with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

graph = networkx.Graph()
for line in lines:
    splitted = line.split(": ")
    for cmp in splitted[1].split():
        graph.add_edge(splitted[0], cmp)

cut_thing = networkx.minimum_edge_cut(graph)
graph.remove_edges_from(cut_thing)
groups = networkx.connected_components(graph)

print("END...", prod([len(group) for group in groups]))
