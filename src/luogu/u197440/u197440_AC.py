#!/usr/bin/python3

# 解题思路：
# 模拟：使用双向链表模拟牌堆洗牌操作
# 时间复杂度: O(K * M)

# 优化数据结构，拉平对象；
# prev[head] 忘记更新了

import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

def cal(x, n, m, k, l, r):
    next = [i + 1 for i in range(0, n)]
    prev = [i - 1 for i in range(0, n)]
    NIL = -1
    next[n - 1] = NIL
    prev[0] = NIL
    head = 0
    for i in range(m):
        now_x = x[i] - 1
        if (prev[now_x] == NIL):
            continue
        o = 0
        end_card = now_x
        while (next[end_card] != NIL) & (o < k):
            end_card = next[end_card]
            o += 1
        next[prev[now_x]] = next[end_card]
        if (next[end_card] != NIL):
            prev[next[end_card]] = prev[now_x]
        
        prev[now_x] = NIL
        next[end_card] = head
        prev[head] = end_card
        head = now_x
 
    for i in range(1, n + 1):
        if (i >= l) and (i <= r):
            print(head + 1)
        head = next[head]
        
def main():
    n, m, k= map(int, input().split())
    x = []
    for i in range(0, m):
        x.append(int(input()))
    l, r = map(int, input().split())
    cal(x, n, m, k, l, r)

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