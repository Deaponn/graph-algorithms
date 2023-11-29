import sys
from queue import PriorityQueue

sys.path.append("..")

from dimacs import loadWeightedGraph
from tester import runtests


def loadGraph(path):
    V, L = loadWeightedGraph(path)
    output = [[0] * V for _ in range(V)]
    for x, y, w in L:
        output[x - 1][y - 1] = w
        output[y - 1][x - 1] = w
    return output


def mergeVertices(x, y, G):
    for v in range(len(G)):
        G[x][v] += G[y][v]
        G[v][x] += G[v][y]
        G[y][v] = G[v][y] = 0
    G[x][y] = G[y][x] = 0


def minimumCutPhase(G):
    n = len(G)
    S = []
    sum_from_S = [0] * n
    processed = [False] * n
    queue = PriorityQueue()
    queue.put((0, 0))
    while not queue.empty():
        _, u = queue.get()
        if not processed[u]:
            processed[u] = True
            S.append(u)
            for v in range(n):
                if G[u][v] != 0:
                    sum_from_S[v] += G[u][v]
                    queue.put((-sum_from_S[v], v))
    s = S[-1]
    t = S[-2]
    mergeVertices(s, t, G)
    return sum_from_S[s]


def minimumCut(G):
    n = len(G)
    smallest_cut = float("inf")
    for step in range(n - 1):
        small_cut = minimumCutPhase(G)
        smallest_cut = min(smallest_cut, small_cut)
    return smallest_cut


def minimumCutWrapper(path):
    G = loadGraph(path)
    return minimumCut(G)


# graph = loadGraph("connectivity/simple")
# print("graph loaded")
# print(minimumCut(graph))
runtests(minimumCutWrapper, "./connectivity/")
