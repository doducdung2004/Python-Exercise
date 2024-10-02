n = int(input())
arr = list(map(int, input().split()))

chi_so_chan = [i for i in range(n) if arr[i] % 2 == 0]
chi_so_le = [i for i in range(n) if arr[i] % 2 != 0]

chan_da_sap_xep = sorted([arr[i] for i in chi_so_chan])
le_da_sap_xep = sorted([arr[i] for i in chi_so_le], reverse=True)

ket_qua = [0] * n
dem_chan = 0
dem_le = 0

for i in range(n):
    if i in chi_so_chan:
        ket_qua[i] = chan_da_sap_xep[dem_chan]
        dem_chan += 1
    else:
        ket_qua[i] = le_da_sap_xep[dem_le]
        dem_le += 1

print(*ket_qua)