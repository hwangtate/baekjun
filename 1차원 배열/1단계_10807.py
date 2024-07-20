N = int(input())

if 1<= N <= 100:

    list = list(map(int,input().split()))

    if len(list) == N:
        v = int(input())
        count = list.count(v)

        print(count)

    else:
        raise IndexError
else:
    raise IndexError