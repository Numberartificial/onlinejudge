#!/usr/bin/python3
import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

def cal(edges, n, rt):
    evs = []
    in_vs= []
    father = []
    max_dep = []
    for i in range(0, n + 1):
        evs.append([])
        in_vs.append(False)
        max_dep.append(0)
        father.append((0, 0))

    for i in range(0, n - 1):
        (u, v, t) = edges[i]
        evs[u].append((v, t))
        evs[v].append((u, t))
    p = 0
    vs = []
    vs.append(rt)
    in_vs[rt] = True
    while (len(vs) < n):
        now_v = vs[p]
        es = evs[now_v]
        for i in range(0, len(es)):
            (u, t) = es[i]
            if (not in_vs[u]):
                in_vs[u] = True
                vs.append(u)
                father[u] = (now_v, t)
        p += 1

    for i in range(n - 1, 0, -1):
        v = vs[i]
        (f, t) = father[v]
        if (t + max_dep[v]) > max_dep[f]:
            max_dep[f] = t + max_dep[v]
    result = 0
    for i in range(n - 1, 0, -1):
        v = vs[i]
        (f, t) = father[v]
        result += max_dep[f] - (max_dep[v] + t)
    return result

def main():
    n = int(input())
    rt = int(input())
    edges = []
    for i in range(0, n - 1):
        (u, v, t) = map(int, input().split())
        edges.append((u, v, t))
    print(cal(edges, n, rt))

if __name__ == "__main__":
    if LOCAL:
        T1 = time.time()
        cwd = os.getcwd()
        file_path = os.path.split(os.path.realpath(__file__))[0]
        sys.stdin = open(file_path + "/hack.in", "r")
        sys.stdout = open(file_path + "/hack.out", "w")
        t = int(input())  # 1
        for i in range(t):
            print(f"Case #{i+1}:", end=' ')
            main()
        T2 = time.time()
        print("Runtime: %.3f s." % (T2 - T1), file=sys.stderr)
    else:
        main()