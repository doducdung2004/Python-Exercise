def sap_xep_va_tinh_tong(S):
    chu_cai = []
    tong_so = 0
    
    for ky_tu in S:
        if ky_tu.isalpha():
            chu_cai.append(ky_tu)
        elif ky_tu.isdigit():
            tong_so += int(ky_tu)
    
    chu_cai.sort()
    ket_qua = ''.join(chu_cai) + str(tong_so)
    return ket_qua

T = int(input())


for _ in range(T):
    S = input().strip()
    print(sap_xep_va_tinh_tong(S))