def count_steps_to_single_digit(n):
    steps = 0
    while len(n) > 1:
        total = sum(ord(digit) - 48 for digit in n)
        n = str(total)
        steps += 1
    return steps

N = input().strip() 
result = count_steps_to_single_digit(N)
print(result)