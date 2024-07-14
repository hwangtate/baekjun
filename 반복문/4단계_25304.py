X = int(input())
N = int(input())

result = 0

while N:
    N -= 1
    a, b = map(int, input().split(' '))
    result += (a * b)

if X == result:
    print("Yes")
elif X != result:
    print("No")