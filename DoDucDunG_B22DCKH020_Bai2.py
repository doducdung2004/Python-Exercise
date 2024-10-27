def l(a):
    n = len(a)
    d = [1] * n  # d[i] lưu chiều dài của chuỗi con không giảm kết thúc tại i

    for i in range(1, n):
        for j in range(i):
            if a[i] >= a[j]:  # Chỉ cần >= để đảm bảo không giảm
                d[i] = max(d[i], d[j] + 1)

    return max(d)  # Chiều dài của chuỗi con không giảm dài nhất

def r(a):
    k = len(a) - l(a)  # Số phần tử cần loại bỏ
    s = []
    d = [1] * len(a)

    # Tìm chuỗi con không giảm
    for i in range(len(a)):
        for j in range(i):
            if a[i] >= a[j]:
                d[i] = max(d[i], d[j] + 1)

    # Xây dựng chuỗi con không giảm
    m = max(d)
    for i in range(len(a) - 1, -1, -1):
        if d[i] == m:
            s.append(a[i])
            m -= 1

    s.reverse()  # Đảo ngược để có thứ tự đúng
    return k, s

# Ví dụ sử dụng
i = [float(i) for i in input().split()]
k, result = r(i)

print(k)
print(result)