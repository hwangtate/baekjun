count = 0
list = []

while count != 9:
    result = int(input())
    list.append(result)
    count += 1

print(max(list))
print(list.index(max(list)) + 1)