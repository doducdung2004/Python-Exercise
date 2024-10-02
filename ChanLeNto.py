import math 
def isValid(n) :
    for i in range(2,int(math.sqrt(n)) + 1 ):
        if n%i ==0 :
            return False 
    return True  
    
for t in range(int(input())) :
    a= input() 
    ok  = 0
    cnt = 0 

    arr = list(int(i) for  i in a) 
    for  i in range(len(arr)) :
        cnt  += arr[i] 
        if i%2 !=0 and arr[i] %2 == 0 :
            ok += 1 
        elif  i%2 ==0 and arr[i] %2 != 0 :
            ok += 1
    if isValid(cnt) == False :
         ok += 1 
    if ok !=0 :
        print('NO')
    else :
        print ('YES')          
 