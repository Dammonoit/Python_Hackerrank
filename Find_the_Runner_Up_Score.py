## question link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    fl=list(arr)
    print(fl[(len(fl)-2)])
