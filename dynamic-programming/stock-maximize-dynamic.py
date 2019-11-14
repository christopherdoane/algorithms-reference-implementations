#!/bin/python3

import math
import os
import random
import re
import sys


# Each day may either:
# 1: buy a share
# 2: sell any number of shares you own
# 3: or not make any transaction at all
# what is the maximum profit you can obtain?

# cool problem, but not realistic.

def maxStockResult(prices):

    lastIndex = len(prices) - 1
    # we want to construct an array of maximums to the right of each element.
    # thus we have pretty much solved if we should buy or sell or do nothing on a given element
    maxToTheRight = [0]*(len(prices)) # our tabular cache
    
    maxToTheRight[lastIndex] = 0 # base case! can't sell after the last day
    maxToTheRight[lastIndex-1] = prices[lastIndex] # base case 2: highest after second-to-last is always the last
    
    for i in range(lastIndex - 2, -1, -1):
        maxToTheRight[i] = max(prices[i+1], maxToTheRight[i+1])
    
    print(*maxToTheRight)

    # Now we step through each day, buying and selling accordingly
    numStocks = 0
    maxProfit = 0
    for i in range(0, len(prices)):
        if maxToTheRight[i] > prices[i]: # only want to buy if we can sell it higher later
            maxProfit -= prices[i] # buy 1
            numStocks += 1
        elif maxToTheRight[i] <= prices[i]: # current price is highest for the remaining of the "relative" series
            maxProfit += numStocks * prices[i] # sell all
            numStocks = 0
    return maxProfit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = maxStockResult(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
