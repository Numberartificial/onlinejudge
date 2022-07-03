#!/usr/bin/python3
import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

def cal(n, a):
    f = [-1 for i in range(n + 1)]
    f[0] = 0
    result = 0
    last_sum = 0
    last_min = 0
    for i in range(n):
        if (last_sum + a[i] >= 0):
            last_sum += a[i]
            if (a[i] < last_min):
                last_min = a[i]
            result += 1
        else:
            if (a[i] > last_min):
                last_sum += a[i] - last_min
                last_min = a[i]

    # for i in range(n):
    #     last_max = result
    #     for k in range(last_max + 1, 0, -1):
    #         if (f[k - 1] < 0):
    #             continue
    #         else:
    #             if (f[k - 1] + a[i]) >= 0:
    #                f[k] = max(f[k], f[k - 1] + a[i])
    #                result = max(result, k)

    # new_a = []
    # i = 0
    # while i < n:
    #     if (a[i] < 0):
    #         new_a.append((a[i], 1))
    #     else:
    #         sa = a[i]
    #         o = 1
    #         while (i < n - 1) & (a[i + 1] >= 0):
    #             i += 1
    #             o += 1
    #             sa += a[i]
    #         new_a.append((sa, o))
    #     i += 1

    # fs[0] = (0, 0)
    # for i in range(len(new_a)):
    #     (ai, oi) = new_a[i]
    #     if (ai >= 0):
    #         for j in range(len(fs)):
    #             (aj, oj) = fs[j]
    #             new_o = oj + oi
    #             f[new_o] = max(f[new_o], aj + ai)
    #             fs[j] = (f[new_o], oj + oi)
    #     else:

    
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