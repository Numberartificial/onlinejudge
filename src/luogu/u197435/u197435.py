#!/usr/bin/python3

# 解题思路：
# 直接看作两个 [1, n/2]全排列的拼接
# 题目中关于字典序的描述与样例输出好像有些问题,以样例的方式
# 按照字典序小的优先输出
# 时间复杂度: O((N / 2)! * (N/2)!)
# 本地测 N = 12 需要 0.7S, python还是比较慢

import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

all_p = []
all_p2 = []

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def dfs(a, dep, k):
    if (dep == k):
        all_p.append(a[:])
        all_p2.append(list(map(lambda x:x + k, a)))

    for i in range(dep, len(a)):
        swap(a, dep, i)
        dfs(a, dep + 1, k)
        swap(a, dep, i)

def print_line(a, b, k):
    print(' '.join(map(str, a)), end=' ')
    print(' '.join(map(str, b)))
    # for x in a:
    #     print(x, end=' ')
    # for x in b:
    #     print(x + k, end=' ')
    # print()

def cal(n):
    k = int(n / 2)
    a = []
    for i in range(0, k):
        a.append(i + 1)
    dfs(a, 0, k)
    for i in range(0, len(all_p)):
        for j in range(0, len(all_p2)):
           print_line(all_p[i], all_p2[j], k) 

def main():
    n = int(input())
    cal(n)

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