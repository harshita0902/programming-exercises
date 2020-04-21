#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    Sum = sum(int(s) for s in n)
    if Sum*k < 10:
        return Sum*k
    else:
        return superDigit(str(Sum*k), 1)
    


if __name__ == '__main__':
    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)
    print(result)
