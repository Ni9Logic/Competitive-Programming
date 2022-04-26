#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    b = []
    for k in a:
        if k not in b:
            b.append(k)
    counters = [int()] * len(b)
    for j, i in enumerate(a):
        if i in b:
            counters[b.index(i)] += 1
    print(b[counters.index(1)])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    lonelyinteger(a)
