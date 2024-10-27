def get_num(n) :
    b = []
    res =''
    for  i in  n :
        if i.isalpha() :
            res +=' '
        elif i.isdigit() :
            res += i 
    for i in res.split() :
        b.append(int(i))
    return b             





ans  = [] 
for t in range(int(input())) :
    s = input()
   
    ans+= get_num(s)
ans.sort()
for i in ans :
    print(i)

