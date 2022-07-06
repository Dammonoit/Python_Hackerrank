if __name__ == '__main__':
    n = int(input())
    output_list=list()
    for i in range(n):
        user_input=input().strip().split(" ")
        if (user_input[0]=='append'):
            output_list.append(int(user_input[1]))
        elif (user_input[0]=='insert'):
            output_list.insert(int(user_input[1]),int(user_input[2]))
        elif (user_input[0]=='print'):
            print(output_list)
        elif (user_input[0]=='remove'):
            output_list.remove(int(user_input[1]))
        elif (user_input[0]=='pop'):
            output_list.pop()
        elif (user_input[0]=='reverse'):
            output_list.reverse()
        elif (user_input[0]=='sort'):
            output_list.sort()
        else:
            pass
    
