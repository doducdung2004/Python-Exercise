def is_suitable(A, B):
    A.sort()
    B.sort()
    for a, b in zip(A, B):
        if a > b:
            return "NO"
    return "YES"


def main():
    T = int(input())
    results = []
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        results.append(is_suitable(A, B))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
