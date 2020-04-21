#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    total = 0
    prev = -1
    for i in s:
        if i == prev:
            total += 1
        prev = i
    return total
    
        
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)