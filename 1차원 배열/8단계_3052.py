remainder_value = [int(input()) for _ in range(10)]
result = []

for i in remainder_value:
    result.append(i % 42)

result = set(result)
clone_result = result

print(len(result & clone_result))

#set(remainders)는 리스트 remainders를 집합으로 변환합니다. 집합은 중복된 요소를 허용하지 않으므로, 이 과정에서 중복된 나머지 값이 제거됩니다.
#그렇기 떄문에... 아래 코드로 최적화 가능합니다...

# # 10개의 숫자를 입력받아 리스트로 저장
# numbers = [int(input()) for _ in range(10)]
#
# # 나머지 리스트 생성
# remainders = [num % 42 for num in numbers]
#
# # 서로 다른 나머지 값의 개수 출력
# unique_remainders = len(set(remainders))
# print(unique_remainders)
