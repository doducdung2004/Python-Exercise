for t in range(int(input())) :
    n= int(input())
    m , cnt = {} , 0 
    for i in range(n) :
         a = int(input())
         if a in m :
            m[a] += 1 
         else :
            m[a] = 1 
         cnt = max(cnt ,m[a])    
    ans = 1000 
    for i in m :
        if  m[i] == cnt :
            ans = min(ans,i) 
        print(ans)                  