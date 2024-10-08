def sort_even_odd(arr):
    
    evens = sorted([x for x in arr if x % 2 == 0])
    odds = sorted([x for x in arr if x % 2 != 0], reverse=True)
    even_index, odd_index = 0, 0
    result = []

    for num in arr:
        if num % 2 == 0:
            result.append(evens[even_index])
            even_index += 1
        else:
            result.append(odds[odd_index])
            odd_index += 1

    return result

n = int(input().strip()) 
A = list(map(int, input().strip().split()))  

result = sort_even_odd(A)
print(" ".join(map(str, result)))