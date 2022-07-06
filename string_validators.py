##question : https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    digit=[(i.isdigit()) for i in s]
    alnum=[(i.isalnum()) for i in s]
    alpha=[(i.isalpha()) for i in s]
    lower=[(i.islower()) for i in s]
    upper=[(i.isupper()) for i in s]
    if True in alnum:
        print("True")
    else:
        print("False")
    if True in alpha:
        print("True")
    else:
        print("False")
    if True in digit:
        print("True")
    else:
        print("False")
    if True in lower:
        print("True")
    else:
        print("False")
    if True in upper:
        print("True")
    else:
        print("False")
    
    

    
    
