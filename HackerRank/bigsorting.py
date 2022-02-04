#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def SortingBigIntegers(arr):
    arr.sort(key = lambda x: (len(x), x))
    print ("\n".join(arr))
        
    return unsorted
if __name__ == '__main__':
    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    SortingBigIntegers(unsorted)
