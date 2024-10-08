n= int(input())
while  n > 0 :
     k = input()
     res  =  -1
     s = 0 
     l = len(k)
     for i in range(0,l-1) :
        if k[i].isdigit() :
            s = s*10 + int(k[i])
            if k[i+1].isalpha() :
                res = max(res,s) 
                s = 0 
     print(max(res,s)) 
     n = -1            
