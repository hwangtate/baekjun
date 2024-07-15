import sys

T = int(sys.stdin.readline().rstrip())
result = []

if T <= 1000000:

    for i in range(T):
        A, B = sys.stdin.readline().strip().split(' ')
        A , B = int(A), int(B)

        if 1 <= A <= 1000 and 1 <= B <= 1000:
            result.append(A+B)

    for i in range(len(result)):
        print(result[i])
