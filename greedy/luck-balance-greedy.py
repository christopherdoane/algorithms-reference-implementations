#!/bin/python

import math
import os
import random
import re
import sys

# lose all unimportant contests
# choose to win the lowest value important contest worth 1 luck

# Parameters:

# contents - 2D array of integers where each contests[i]
# contains two integers that represent the luck balance
# and important of the ith contest

# k = number of important contests Lena can lose

# Complete the luckBalance function below.
def luckBalance(k, contests):
    # numberOfGamesToLose = # important contests - k
    # if negative or 0, can lose all
    # else win in order, the least expensive important contests

    # lose all unimportant games
    # then only win the cheapest (lowest luck bonus modifier)

    numImportant = 0
    resultLuck = 0
    importantGamesLuck = []

    for i in range(0, len(contests)):
        entryLuck = contests[i][0]
        if contests[i][1] == 1:
            numImportant += 1
            importantGamesLuck.append(entryLuck)
        else:
            resultLuck += entryLuck # lose all unimportant
    numberOfGamesToWin = numImportant - k

    importantGamesLuck.sort()
    for i in range(0, len(importantGamesLuck)):
        if numberOfGamesToWin > 0:
            resultLuck -= importantGamesLuck[i]
            numberOfGamesToWin -= 1
        else:
            resultLuck += importantGamesLuck[i]

    return resultLuck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in xrange(n):
        contests.append(map(int, raw_input().rstrip().split()))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
