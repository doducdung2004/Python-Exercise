for t in range(int(input())):
    a = int(input()) 
    ok = 0 
    if a %2 ==0 :
        for  i in range(2,a+1,2) :
            ok = ok + 1/i
        print('{:.6f}'.format(ok))    
    else :
        for i in range(1,a+1,2) :
            ok = ok + 1/i
        print('{:.6f}'.format(ok))     