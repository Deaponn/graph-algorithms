import sys

sys.path.append("..")

from dimacs import *


def find(member, find_union):
    if member != find_union[member]:
        find_union[member] = find(find_union[member], find_union)
    return find_union[member]


def union(first, second, find_union, ranks):
    if ranks[first] > ranks[second]:
        find_union[second] = first
    else:
        find_union[first] = second
        if ranks[first] == ranks[second]:
            ranks[second] += 1


def min_of_max(s, t, n, G):
    find_union = list(range(n + 1))
    ranks = [1] * (n + 1)
    s_rep = s
    t_rep = t
    for v, u, cost in G:
        v_rep = find(v, find_union)
        u_rep = find(u, find_union)
        if v_rep != u_rep:
            union(v_rep, u_rep, find_union, ranks)
            s_rep = find(s, find_union)
            t_rep = find(t, find_union)
            if s_rep == t_rep:
                return cost
    return G[-1][2]


V, L = loadWeightedGraph("./graphs/clique1000")

L.sort(key = lambda edge: -edge[2])

s = 1
t = 2

print(min_of_max(s, t, V, L))
