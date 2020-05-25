#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c1=0
    c2=0
    for i in apples:
        if i>=0:
            if (i+a)>=s and (i+a)<=t:
                c1=c1+1
    for i in oranges:
        if i<=0:
            if (i+b)<=t and (i+b)>=s:
                c2=c2+1
    print(c1)
    print(c2)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
