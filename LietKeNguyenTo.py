import math 
def isValid(n) :
    for i in range(2,int(math.sqrt(n)) + 1 ):
        if n%i ==0 :
            return False 
    return True  
a = int(input()) 
arr = list(int(i) for i in input().split())
b = {}
for i in range(len(arr)) :
    if isValid(arr[i]) :
        if arr[i] in b :
            b[arr[i]]  += 1
        else :
            b[arr[i]] = 1 
for i in b :
    print(i, ' ', b[i])
        
