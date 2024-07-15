N = int(input())
text = "long "
count = 0

if 4 <= N <= 1000 and N % 4 == 0 :

    for i in range(int(N / 4)):
        count += 1

    print(f"{text * count}int")