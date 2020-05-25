

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(sc,s,ac,a):
    s=set(s)
    s=list(s)
    s.sort()
    s=s[::-1]
    i=0
    j=0
    sc=len(s)
    while i<ac:
        while j<sc:
            if a[i]>=s[j]:
                print(j+1)
                break
            else:
                j=j+1
        if j==sc:
            print(j+1)
        j=0
        i=i+1

sc = int(input())

scores = list(map(int, input().rstrip().split()))

ac = int(input())

alice = list(map(int, input().rstrip().split()))

climbingLeaderboard(sc,scores,ac,alice)
