def mintriple(lst):
    unique_set = set(lst)

    if len(unique_set) < 3:
        return sum(unique_set)
    
    min1 = min(unique_set)
    unique_set.remove(min1)
    
    min2 = min(unique_set)
    unique_set.remove(min2)
    
    min3 = min(unique_set)
    
    return min1 + min2 + min3

for t in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(mintriple(lst))