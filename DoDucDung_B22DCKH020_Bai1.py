def hinhvuong(m):
    if not m or not m[0]:
        return 0
    # Kiểm tra nếu ma trận không tồn tại hoặc cột của ma trận không có thì thoát chương trình
    r = len(m)
    # r = số hàng 
    c = len(m[0])
    # c = số cột 
    x = 0
    d = [[0] * c for _ in range(r)]
    # sử dụng ma trận d để đánh dấu vị trí xuất hiện 1 trong ma trận m 
    bottom_right = (0, 0)  # Tọa độ góc dưới bên phải của hình vuông lớn nhất

    for i in range(r):
        for j in range(c):
            if m[i][j] == 1:
                if i == 0 or j == 0:
                    d[i][j] = 1
                else:
                    d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
                if d[i][j] > x:  # Cập nhật kích thước và tọa độ nếu tìm thấy hình vuông lớn hơn
                    x = d[i][j]
                    bottom_right = (i, j)  # Cập nhật tọa độ

    # Tính toán tọa độ các góc
    top_left = (bottom_right[0] - x + 1, bottom_right[1] - x + 1)
    top_right = (top_left[0], bottom_right[1])
    bottom_left = (bottom_right[0], top_left[1])

    
    return x * x  , top_right , top_left , bottom_left , bottom_right 

def hinhchunhat(m):
    if not m or not m[0]:
        return 0
    # Kiểm tra nếu ma trận không tồn tại hoặc cột của ma trận không có thì thoát chương trình
    r = len(m)
    # r = số hàng 
    c = len(m[0])
    a = 0
    # Biến để lưu diện tích lớn nhất
    h = [0] * c
    # Danh sách lưu chiều cao tích lũy cho từng cột
    bottom_right = (0, 0)  # Tọa độ góc dưới bên phải của hình chữ nhật lớn nhất

    for i in range(r):
        for j in range(c):
            if m[i][j] == 1:
                h[j] += 1
            else:
                h[j] = 0

        current_area = area(h)
        if current_area > a:  # Cập nhật diện tích và tọa độ nếu tìm thấy hình chữ nhật lớn hơn
            a = current_area
            bottom_right = (i, h.index(max(h)))  # Lấy tọa độ góc dưới bên phải dựa trên chiều cao

    # Tính toán tọa độ các góc
    height = max(h)
    width = current_area // height
    top_left = (bottom_right[0] - height + 1, bottom_right[1] - width + 1)
    top_right = (top_left[0], top_left[1] + width - 1)
    bottom_left = (bottom_right[0], top_left[1])

   
    return a  , top_right , top_left , bottom_left , bottom_right 

def area(h):
    s = []
    a = 0
    h.append(0)
    for i in range(len(h)):
        while s and h[s[-1]] > h[i]:
            height = h[s.pop()]
            width = i if not s else i - s[-1] - 1
            a = max(a, height * width)
        s.append(i)
    return a

k = int(input())
n = int(input())
a = []
for i in range(0, k):
    b = list(map(int, input().split()))
    a.append(b)

print(hinhvuong(a))
print(hinhchunhat(a))