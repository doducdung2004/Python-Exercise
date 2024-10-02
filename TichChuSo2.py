import math 

def isValid(n) :
    if  n < 2 :
        return False 
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i ==0 :
                return False 
        return True 


for t in range(int(input())):
    a = input()
    arr = list(int(i) for i in a)
    tich = 1
    tong = 0
    for i in range(len(arr)):
        if i %2 ==0 and arr[i]!= 0 :
            tich *= arr[i] 
        else :
            tong += arr[i]

    print(str(tich) + ' ' + str(tong))        



        