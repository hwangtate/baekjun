T = int(input())
result = []

for i in range(T):
    A, B = map(int, input().split())
    
    if 0 < A and B < 10:
        result.append(A + B)

for t in range(len(result)):
    print(f"Case #{t+1}: {result[t]}") 
