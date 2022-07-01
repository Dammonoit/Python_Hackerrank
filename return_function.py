##question link : https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

def printf(num):
    for i in range(1,num+1):
        print(i,end="")

if __name__ == '__main__':
    n = int(input())
    printf(n)
