#!/bin/python3
## question link : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
import math
import os
import random
import re
import sys

def task(n):
    if (n%2!=0):
        print("Weird")
    elif ((n%2==0) and (2<=n<=5)):
        print("Not Weird")
    elif ((n%2==0) and (6<=n<=20)):
        print("Weird")
    elif ((n%2==0) and (n>=20)):
        print("Not Weird")
        
        
        
        
        
    
if __name__ == '__main__':
    n = int(input().strip())
    task(n)
