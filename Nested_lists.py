## question link : https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp=list()
        temp.append(name)
        temp.append(score)
        l.append(temp)
    print(l)
    score_list=list()
    for i in range(0,len(l)):
        score_list.append(l[i][1])
