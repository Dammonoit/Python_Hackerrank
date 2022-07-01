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
    print(score_list)
    score_list=sorted(score_list,reverse=True)
    final_list=[]
    for i in range(0,len(l)):
        if score_list[-1]==l[i][1]:
            final_list.append(l[0][i])
        elif score_list[-2]==l[i][1]:
            final_list.append(l[0][i])
        else:
            pass
   for i in sorted(score_list):
       print(i)
    
        
