def tim_phan_tu_chung(A, B, C):
    i, j, k = 0, 0, 0
    ket_qua = []

    while i < len(A) and j < len(B) and k < len(C):
        if A[i] == B[j] == C[k]:
            ket_qua.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        else:
            k += 1

    return ket_qua

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    phan_tu_chung = tim_phan_tu_chung(A, B, C)
    
    if phan_tu_chung:
        print(*phan_tu_chung)
    else:
        print("NO")