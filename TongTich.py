for t in range(int(input())): 
    a  = input() 
    arr = [int(i) for i in a]
    cnt = 0 
    ans  = 1
    for i in range(len(arr)):
        if i %2 == 0 :
            cnt += arr[i] 
        elif i %2 != 0  and arr[i] != 0 :
            ans *= arr[i]  
    print(cnt  , " ", ans)
   
