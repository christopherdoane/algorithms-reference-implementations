#!/bin/python3

import math
import os
import random
import re
import sys

# Determine the number of ways of making change for a particular
# number of units using the given types of coins

def numWays(n, c):
    amountToMakeChangeFor = n
    coinTypes = c
    coinTypes.sort() # typically in dynamic problems we sort to make the smallest of subproblems come up first
    cache = {} # almost always have a cache in dynamic programming (tabular) if doing it iteratively
    cache[0] = 1
    for coinType in coinTypes:
        for subproblem in range(0, n+1):
            # coin cant be larger than the big goal AND cant be larger than the current subproblem
            if amountToMakeChangeFor >= coinType and subproblem >= coinType:
                if subproblem not in cache:
                    cache[subproblem] = 0 # initialize the subproblem
                if (subproblem - coinType) not in cache:
                    cache[subproblem - coinType] = 0 # initialize for subproblems not possible, we could also check if this subsub problem existed or not and skip it otherwise
                # we then use the coinType, and add on the subproblem that is equal to the current subproblem - the coin. 
                # If we never solved the subsubproblem, then the initial value of 0 will be added.
                cache[subproblem] += cache[subproblem - coinType] 

    if amountToMakeChangeFor in cache:
        return cache[amountToMakeChangeFor]
    return 0 # if we were not able to build up subproblems to our final goal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    ways = numWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
