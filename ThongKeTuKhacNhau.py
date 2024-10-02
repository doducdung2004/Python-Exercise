import re
from collections import Counter

def xu_ly_van_ban(van_ban):
    # Chuyển thành chữ thường và loại bỏ dấu câu
    van_ban = van_ban.lower()
    van_ban = re.sub(r'[.,?!:;\(\)\-/]', ' ', van_ban)
    # Tách thành các từ và loại bỏ chuỗi rỗng
    return [tu for tu in van_ban.split() if tu]

n = int(input())
danh_sach_tu = []

for _ in range(n):
    dong = input()
    danh_sach_tu.extend(xu_ly_van_ban(dong))

so_lan_xuat_hien = Counter(danh_sach_tu)

# Sắp xếp từ theo số lần xuất hiện (giảm dần) và theo thứ tự từ điển
tu_da_sap_xep = sorted(so_lan_xuat_hien.items(), key=lambda x: (-x[1], x[0]))

# In kết quả
for tu, so_lan in tu_da_sap_xep:
    print(f"{tu} {so_lan}")