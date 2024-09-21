for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    

    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    

    max_count = 0
    result = "NO"
    for num, freq in count.items():
        if freq > n // 2 and freq > max_count:
            max_count = freq
            result = num
    
    print(result)