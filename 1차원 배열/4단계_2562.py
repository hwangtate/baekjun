# 입력 받기
numbers = [int(input()) for _ in range(9)]

# 최댓값과 최댓값의 위치 찾기
max_value = max(numbers)
max_index = numbers.index(max_value) + 1  # index는 0부터 시작하므로 +1

# 결과 출력
print(max_value)
print(max_index)
