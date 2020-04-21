#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = []
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j],2))) for j in b]))
    return sum(count)
    

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)
