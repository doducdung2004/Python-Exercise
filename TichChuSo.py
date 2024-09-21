for t in range(int(input())):
    n = input() 
    arr = [int(i) for i in n]
    ans = 1 
    for i in arr:
        if i != 0:
            ans *=i 
    print(ans)
