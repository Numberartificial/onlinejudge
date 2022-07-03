#!/usr/bin/python3

# 解题思路：
# 模拟：使用双向链表模拟牌堆洗牌操作
# 时间复杂度: O(K * M)

import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

class Card:
    v = 0
    next = None
    prev = None

    def __init__(self, v):
        self.v = v

def cal(x, n, m, k, l, r):
    cards = []
    last = None
    for i in range(n):
        card = Card(i)
        if (last != None):
            last.next = card
            card.prev = last
        last = card
        cards.append(card)
    head = cards[0]

    for i in range(m):
        now_x = x[i] - 1
        now_card = cards[now_x]
        if (now_card.v == head.v):
            continue
        o = 0
        end_card = now_card
        while (end_card.next is not None) & (o < k):
            end_card = end_card.next
            o += 1
        if (now_card.prev is not None):
            now_card.prev.next = end_card.next
        if (end_card.next is not None):
            end_card.next.prev = now_card.prev
        now_card.prev = None
        end_card.next = head
        head = now_card
    
    for i in range(1, n + 1):
        if (i in range(l, r + 1)):
            print(head.v + 1)
        head = head.next
        
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