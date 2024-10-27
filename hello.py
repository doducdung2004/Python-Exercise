def find(n,k) :
    def helper(n,k) :
        if n ==1 :
            return 'A'
        mid = 2**(n-1)
        if k == mid :
            return chr(64+n)
        elif k < mid :
            return helper(n-1,k)
        else :
            return helper(n-1,k-mid)
    return helper(n,k)

t = int(input())
for t in range(t) :
    a = []
    n,k = map(int,input().split())
    a.append(find(n,k))
    for af in a :
        print(af)
