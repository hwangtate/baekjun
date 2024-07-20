# 입력 받기
N, X = map(int, input().split())
A = list(map(int, input().split()))

# X보다 작은 수를 저장할 리스트 생성
result = []

# 수열 A를 순회하며 X보다 작은 수를 결과 리스트에 추가
for number in A:
    if number < X:
        result.append(number)

# 결과 출력
print(" ".join(map(str, result)))
