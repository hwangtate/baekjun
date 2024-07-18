T = int(input())

result = []

for i in range(T):
    A, B = map(int, input().split())
    C = A + B
    x = i + 1
    result.append(f"Case #{x}: {A} + {B} = {C}")

for i in range(T):
    print(result[i])