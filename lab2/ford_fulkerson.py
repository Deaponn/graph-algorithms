import sys

sys.path.append("..")

from dimacs import loadDirectedWeightedGraph


def loadGraph(path):
    V, L = loadDirectedWeightedGraph(path)
    output = [[0] * V for _ in range(V)]
    for x, y, w in L:
        output[x - 1][y - 1] = w
    return output


def dfs_finder(s, t, G):
    n = len(G)
    visited = [False] * n
    parents = [None] * n

    def dfs_visit(v, t, current_volume, visited, parents, G):
        if v == t:
            return current_volume, True
        if not visited[v]:
            visited[v] = True
            for w in range(n):
                if G[v][w] > 0:
                    path_volume, success = dfs_visit(w, t, min(G[v][w], current_volume), visited, parents, G)
                    if success:
                        parents[w] = v
                        return path_volume, True
        return 0, False

    volume, success = dfs_visit(s, t, float("inf"), visited, parents, G)
    return volume, parents, success


def bfs_finder(s, t, G):
    n = len(G)
    visited = [False] * n
    parents = [None] * n
    queue = []
    queue.append(s)

    while len(queue) > 0:
        v = queue.pop(0)
        t_found = False
        if not visited[v]:
            visited[v] = True
            for w in range(n):
                if parents[w] is None and G[v][w] > 0:
                    parents[w] = v
                    queue.append(w)
                    if w == t:
                        t_found = True
                        break
        if t_found:
            break
    if parents[t] is None:
        return 0, parents, False
    volume = float("inf")
    u, v = parents[t], t
    while v != s:
        volume = min(G[u][v], volume)
        u, v = parents[u], u
    return volume, parents, True


def ford_fulkerson(s, t, G, path_finder):
    volume = 0
    while True:
        new_volume, path, can_wider = path_finder(s, t, G)
        if not can_wider:
            break
        volume += new_volume
        u, v = path[t], t
        while v != s:
            G[u][v] -= new_volume
            G[v][u] += new_volume
            u, v = path[u], u
    return volume


G1 = loadGraph("flow/rand20_100")
G2 = loadGraph("flow/rand20_100")
s = 0
t = len(G1) - 1

print(ford_fulkerson(s, t, G1, dfs_finder))
print(ford_fulkerson(s, t, G2, bfs_finder))
