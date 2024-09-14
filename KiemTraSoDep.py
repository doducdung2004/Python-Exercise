for r in range(int(input())) :
    a = input() 
    ok = 0 
    for i in range(2,len(a)) :
        if ( a[i] != a[i-2]) :
             ok = ok + 1 
    if ok == 0 : 
        print('YES')
    else :
        print('NO')             
