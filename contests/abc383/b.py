h, w, d = list(map(int, input().split()))
s = [list(input()) for _ in range(h)]

ans = 0
for i1 in range(h):
    for j1 in range(w):
        for i2 in range(h):
            for j2 in range(w):
                if i1 == i2 and j1 == j2:
                    continue
                if s[i1][j1] == "#" or s[i2][j2] == "#":
                    continue

                cnt = 0
                for i in range(h):
                    for j in range(w):
                        if s[i][j] == "#":
                            continue
                        is_humid = False
                        if abs(i - i1) + abs(j - j1) <= d:
                            is_humid = True
                        if abs(i - i2) + abs(j - j2) <= d:
                            is_humid = True
                        if is_humid:
                            cnt += 1
                ans = max(ans, cnt)
print(ans)
