#!/bin/python

import math
import os
import random
import re
import sys

# Given an array of integers, find and print the minimum absolute
# difference between any two elements in the array.

def minAbsDiff(arr):
    minDiff = sys.maxsize
    # sort elements
    arr.sort() # inplace! returns None if you assign the result to something
    # compare element wise, moving elem 1 tracker and elem 2 tracker
    for i in range(0, len(arr) - 1):
        localDiff = abs(arr[i] - arr[i+1])
        if localDiff < minDiff:
            minDiff = localDiff
    return minDiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = minAbsDiff(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
