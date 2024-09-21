n = int(input())
a = [int(i) for i in input().split()] 
a.sort() 
for i in a: 
    if i + 1 not in a: 
        print(i+1)
        break