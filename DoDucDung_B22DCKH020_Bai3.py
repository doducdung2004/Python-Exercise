def  isvalid(a):
    # Khởi tạo dp
    dp = [[0] * 5 for _ in range(a + 1)]
    
    # Khởi tạo cho độ dài 0
    dp[0] = [1, 1, 1, 1, 1]  # a, e, i, o, u

    for length in range(1, a + 1):
        # Tính số chuỗi cho từng nguyên âm
        dp[length][0] = dp[length - 1][1]  # a -> e
        dp[length][1] = dp[length - 1][0] + dp[length - 1][2]  # e -> a, i
        dp[length][2] = dp[length - 1][0] + dp[length - 1][1] + dp[length - 1][3] + dp[length - 1][4]  # i -> a, e, o, u
        dp[length][3] = dp[length - 1][4] + dp[length - 1][2]  # o -> u, i
        dp[length][4] = dp[length - 1][0]  # u -> a

    # Tổng số chuỗi hợp lệ có độ dài N
    return sum(dp[a])

n = int(input())
result = isvalid(n)
print(f"{result}" + ' chuỗi')