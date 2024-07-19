result = []
testcase = 0

while testcase == 0:
    A, B = map(int, input().split())
    
    if A == 0 or B == 0:
        testcase += 1 
        continue

    result.append(A + B)

for i in range(len(result)):
    print(result[i])