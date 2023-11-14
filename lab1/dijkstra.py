# ----------- NOT A WORKING IMPLEMENTATION -------------


import sys
from queue import PriorityQueue

sys.path.append("..")

from dimacs import *


def edge_list_to_neighbours_list(G, n):
    output = [[] for _ in range(n)]
    for v, u, cost in G:
        output[v - 1].append((u - 1, cost))
        output[u - 1].append((v - 1, cost))
    return output


def min_of_max(s, t, G):
    # this is essentially a reversed dijkstra, since we look for a max-weighted path instead of min-weighted
    queue = PriorityQueue()
    for v, cost in G[s]:
        queue.put((v, -cost))
    pass


V, L = loadWeightedGraph("./graphs/path10000")

G = edge_list_to_neighbours_list(L, V)

s = 1
t = 2

print(min_of_max(s, t, G))
