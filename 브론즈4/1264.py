vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
results = []
result = 0

while True:
    N = input()

    if N == '#':
        break

    for i in vowel:
        result += N.count(i)

    results.append(result)
    result = 0

for i in results:
    print(i)