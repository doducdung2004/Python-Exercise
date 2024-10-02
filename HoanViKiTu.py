from itertools import permutations
def hoanvi(s) :
    hoan_vi = [''.join(p) for p in permutations(s)] 
    hoan_vi.sort() 
    for i in hoan_vi :
        print(i)

s = input().strip() 
hoanvi(s) 