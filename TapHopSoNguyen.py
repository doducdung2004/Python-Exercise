def doc_va_tao_tap_hop():
    return set(map(int, input().split()))

def in_tap_hop(tap_hop):
    print(*sorted(tap_hop))


n, m = map(int, input().split())

A = doc_va_tao_tap_hop()
B = doc_va_tao_tap_hop()


giao = A.intersection(B)
hieu_A_B = A.difference(B)
hieu_B_A = B.difference(A)


in_tap_hop(giao)
in_tap_hop(hieu_A_B)
in_tap_hop(hieu_B_A)