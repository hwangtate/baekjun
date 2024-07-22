submit_students = [int(input()) for _ in range(28)]
success_students = [i for i in range(1, 31)]
no_students = []

for i in success_students:
    if i not in submit_students:
        no_students.append(i)


print(min(no_students))
print(max(no_students))

