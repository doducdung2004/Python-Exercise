a , k , n = map(int,input().split())
if  k > n :
    print(-1)
else :
    x =  k - a % k 
    if a + x > n :
        print(-1)
    else :
        for i in range(x, n-a+1 , k):
            print(i, end = " ")
