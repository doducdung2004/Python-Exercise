from math import gcd

def find_shortest_subarray(A, K):
    N = len(A)
    min_length = float('inf')
    
    for i in range(N):
        agcd = A[i]
        if agcd == K:
            return 1
        
        for j in range(i+1, N):
            gcd = gcd(agcd, A[j])
            if agcd == K:
                min_length = min(min_length, j - i + 1)
                break
            elif agcd < K:
                break
    
    return min_length if min_length != float('inf') else -1

def solve_test_case():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = find_shortest_subarray(A, K)
    print(result)

T = int(input())
for _ in range(T):
    solve_test_case()
