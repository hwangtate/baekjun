T = int(input())
C = []

while T: 
    try:
        T -= 1
        A, B  = map(int, input().split(' '))

        if 0 < A and B < 10:
            C.append((A + B))        
    except ValueError:
        None

for i in range(len(C)):
    print(C[i])