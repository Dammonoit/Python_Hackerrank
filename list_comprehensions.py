## question link : https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                temp=[i,j,k]
                if sum(temp)==n:
                    pass
                else:
                    l.append(temp)
    print(l)


