X = list(map(int, input().split()))
Y = []

for i in range(1 << 5):
    x = ""
    y = 0

    for j in range(5):
        if (i >> j) & 1:
            x += "ABCDE"[j]
            y += X[j]
    Y.append((y, x))

Y.sort(key=lambda x: (-x[0], x[1]))

for i in range(31):
    print(Y[i][1])
