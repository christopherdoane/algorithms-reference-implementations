#!/bin/python

import math
import os
import random
import re
import sys

# ti+2 = ti + (ti+1)^2

# Complete the fibonacciModified function below.
def fibModded(t1, t2, n):
    cache = {}
    cache[0] = t1
    cache[1] = t2
    
    for i in range(2, n):
        # normal fib -> cache[i] = cache[i - 1] + cache[i - 2]
        cache[i] = cache[i - 2] + cache[i - 1] ** 2
    return cache[n-1] # since we start on zero index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = raw_input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibModded(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
