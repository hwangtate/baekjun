remainder_value = [int(input()) for _ in range(10)]
result = []

for i in remainder_value:
    result.append(i % 42)

result = set(result)
clone_result = result

print(len(result & clone_result))

