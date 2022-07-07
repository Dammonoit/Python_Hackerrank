##question : https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

user_input=input().split()
output=[]
for i in list(permutations(sorted(user_input[0]),int(user_input[1]))):
    print("".join(i))
