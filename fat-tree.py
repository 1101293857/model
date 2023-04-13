import random
import json
import copy
import numpy as np


def fat_tree(k):  # return  link and node num
    L1 = int(k / 2) * int(k / 2)
    L2 = int(k / 2) * k
    L3 = L2
    n = int(k / 2)
    c = []
    a = []
    e = []
    Link = []
    # add core ovs
    for i in range(L1):
        c.append(i + 1)

    # add aggregation ovs
    for i in range(L2):
        a.append(L1 + i + 1)

    # add edge ovs
    for i in range(L3):
        e.append(L1 + L2 + i + 1)

    # add links between core and aggregation ovs
    for i in range(L1):
        sw1 = c[i]
        for j in range(i % n, len(a), n):
            Link.append((a[j], sw1))

    # add links between aggregation and edge ovs
    for i in range(0, L2):
        m = int(i / n)
        sw1 = a[i]
        for j in range(n):
            Link.append((e[int(m * (n) + j)], sw1))

    return Link, L1 + L2 + L3


def returnGraph(links, node):
    graph = np.zeros((node, node))
    for i in links:
        graph[i[0] - 1][i[1] - 1] = 1
        graph[i[1] - 1][i[0] - 1] = 1
    return graph


link, n = fat_tree(4)
print(returnGraph(link, n))
