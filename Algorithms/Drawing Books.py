#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    i=1
    s1=0
    s2=0
    while(i<p):
        s1=s1+1
        i=i+2

    if n%2==0:
        while(n>p):
            s2=s2+1
            n=n-2
    else:
        if p==n-1:
            s2=0
        else:
            while(n>p):
                s2=s2+1
                n=n-2
    print(min(s1,s2))

n = int(input())

p = int(input())

result = pageCount(n, p)
