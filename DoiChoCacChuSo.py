def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
for t in range(int(input())) :
    a = input()
    arr = list( int(i) for i in a) 
    ok = False 
    for i in range(len(arr)-1,1,-1) :
        if arr[i]!=arr[i-1] :
            swap(arr ,arr[i],arr[i-1])
            ok = True 
            break 
    if ok == True :
        print(arr)
    else :
        print(-1)    
        