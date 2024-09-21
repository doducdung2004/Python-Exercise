import functools
def product_of_digits(n):
    prod = 1
    for digit in str(n):
        prod *= int(digit)
    return prod

def compare(a, b):
    prod_a = product_of_digits(a)
    prod_b = product_of_digits(b)
    if prod_a == prod_b:
        return a - b
    return prod_a - prod_b

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key=functools.cmp_to_key(compare))
    print(*arr)