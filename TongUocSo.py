def prime_factors_sum(n):
    sum_factors = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            sum_factors += d
            n //= d
        d += 1
    if n > 1:
        sum_factors += n
    return sum_factors

N = int(input())
total_sum = 0

for _ in range(N):
    num = int(input())
    total_sum += prime_factors_sum(num)

print(total_sum)