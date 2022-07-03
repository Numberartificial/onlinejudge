#!/usr/bin/python3
import sys
import os
import time
from functools import reduce
from math import *

LOCAL = not __debug__  # True if compile option '-O'

def cal(n, a):
    result = 0
    max_v = 100 * 100 + 1024
    f_min = [[max_v] * n for i in range(n)]
    f_max = [[-max_v] * n for i in range(n)]
    for i in range(0, n):
        x = int(a[2 * i])
        f_min[i][i] = x
        f_max[i][i] = x

    s = []
    for i in range(1, n):
        s.append(1 if a[2 * i - 1] == '+' else -1)

    for k in range(2, n + 1):
        for i in range(0, n):
            r = min(i + k - 1, n - 1)
            for j in range(i + 1, r + 1):
                if (s[j - 1] == 1):
                    f_max[i][r] = max(f_max[i][r], f_max[i][j - 1] + f_max[j][r])
                    f_min[i][r] = min(f_min[i][r], f_min[i][j - 1] + f_min[j][r])
                else:
                    f_max[i][r] = max(f_max[i][r], f_max[i][j - 1] - f_min[j][r])
                    f_min[i][r] = min(f_min[i][r], f_min[i][j - 1] - f_max[j][r])
    return f_max[0][n - 1]

def main():
    n = int(input())
    a = input().split()
    print(cal(n, a))

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