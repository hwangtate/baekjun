N = int(input())
X = list(map(int, input().split()))

if len(X) == N:
    print(min(X), max(X))
    