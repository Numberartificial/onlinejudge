#!/usr/bin/python3

# 解题思路：
# 首先想的是动规，但是时间复杂度需要 O(N * N)
# 没有想到太好的动规优化
# note: 只有负数是需要关注的，非负数一定是直接加入
# 使用贪心算法，从左至右，当前a[i]能加入则加入，
# 如果不能加入（一定是负数,a[i]<0），那么选择已加入中的最小负数a[j]，
# 如果a[j] < a[i]，则踢除a[j]，将当前的a[i]加入（一定更优：个数不变，生命值更高）
# 时间复杂度: O(N)

# 只拿了20分

# 复盘： 思路应该没问题，删除最小元素那里写错了，需要最小堆。唉。。。

import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

class minheap:
    def __init__(self):
        pass 

def push(g, o):
    g.append(o)
    l = len(g) - 1
    while (l != 0) and (g[(l - 1) // 2] > g[l]):
        k = g[(l - 1) // 2]
        g[(l - 1) // 2] = g[l]
        g[l] = k
        l = (l - 1) // 2

def sink(g):
    l = 0
    n = len(g)
    next = True
    while (l < n) and next:
        next = False
        ll = l * 2 + 1
        rr = l * 2 + 2
        min_idx = l
        if (ll < n) and (g[ll] < g[min_idx]):
            min_idx = ll
        if (rr < n) and (g[rr] < g[min_idx]):
            min_idx = rr
        if (min_idx != l):
            k = g[l]
            g[l] = g[min_idx]
            g[min_idx] = k
            l = min_idx
            next = True

def cal(n, a):
    result = 0
    last_sum = 0
    g = []
    for i in range(n):
        if (last_sum + a[i] >= 0):
            last_sum += a[i]
            result += 1
            if (a[i] < 0):
                push(g, a[i])
        else:
            if len(g) > 0:
                last_min = g[0]
                if (a[i] > last_min):
                    g[0] = a[i]
                    sink(g)
                    last_sum += a[i] - last_min
    
    return result 


def main():
    n = int(input())
    a = list(map(int, input().split()))[0:n]
    print(cal(n, a))

if __name__ == "__main__":
    if LOCAL:
        T1 = time.time()
        cwd = os.getcwd()
        file_path = os.path.split(os.path.realpath(__file__))[0]
        sys.stdin = open(file_path + "/hack.in", "r")
        sys.stdout = open(file_path + "/hack1.out", "w")
        t = int(input())  # 1
        for i in range(t):
            print(f"Case #{i+1}:", end=' ')
            main()
        T2 = time.time()
        print("Runtime: %.3f s." % (T2 - T1), file=sys.stderr)
    else:
        main()