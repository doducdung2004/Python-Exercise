def isValid(s):
    if len(s) < 2:
        return False
    if s != s[::-1]:
        return False
    return True

for t in range(int(input())):
    n = input()
    arr = [int(i) for i in n]
    cnt = 0 
    for i in arr:
        cnt += i
    if isValid(str(cnt)) :     
        print("YES")
    else:
        print("NO")

        