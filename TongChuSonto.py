import math 
def isValid(n) :
    for i in range(2,int(math.sqrt(n)) + 1 ):
        if n%i ==0 :
            return False 
    return True  
for t in range(int(input())) :
    cnt = 0 
    a = input() 
    arr = list(int(i) for i in a) 
    for i in range(len(arr)) :
        cnt += arr[i] 
    if isValid(cnt) :
        print('YES')
    else :
        print('NO')    