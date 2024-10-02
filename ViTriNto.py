def is_prime(n):
    nto = [1] * (n + 1)
    nto[0] = nto[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if nto[i]:
            for j in range(i*i, n + 1, i):
                nto[j] = 0
    return nto

for t in range(int(input())):
    n = input()
    arr = [int(i) for i in n]
    cnt = 0 
    for i in range(len(arr)):
        if is_prime(arr[i]) ==0  and is_prime(i):
            cnt += 1
        elif is_prime(arr[i]) == 0 and is_prime(i) == 0:
            cnt += 1
        elif is_prime(arr[i]) == 1 and is_prime(i) == 0:
            cnt += 1
    if cnt == 0 :
        print('YES')
    else:
        print('NO')

