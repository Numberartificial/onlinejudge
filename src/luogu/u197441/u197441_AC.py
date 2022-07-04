#!/usr/bin/python3

# 解题思路：
# 在K分钟内最多书的方案下，
# 每多在A选择一本书，那么在B可读的书不可能增多，
# 因此使用两个指针顺次移动,贪心完成所有方案的枚举
# 时间复杂度: O(N) + O(M)

import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

def forSum(a):
    for i in range(1, len(a)):
        a[i] = a[i - 1] + a[i]
    return a

def cal(a, b, n, m, k):
    s1 = forSum(a)
    s2 = forSum(b) 
    s1.insert(0, 0)
    s2.insert(0, 0)
    p1 = 0
    p2 = m
    now1 = 0
    result = 0
    while (p2 >= 0) & (p1 <= n):
        while (p2 > 0) & (s1[p1] + s2[p2] > k):
            p2 -= 1
        if (s1[p1] + s2[p2] <= k):
            if (p1 + p2) > result:
                result = p1 + p2
        p1 += 1
    return result

def main():
    n, m, k= map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    print(cal(a1[0:n], a2[0:m],n,m, k))

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