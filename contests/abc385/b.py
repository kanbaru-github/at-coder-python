h, w, x, y = map(int, input().split())

x -= 1
y -= 1

s = [list(input()) for _ in range(h)]
t = input()

ans = 0
for i in range(len(t)):
    ni, nj = x, y
    if t[i] == "U":
        ni -= 1
    if t[i] == "D":
        ni += 1
    if t[i] == "L":
        nj -= 1
    if t[i] == "R":
        nj += 1

    if s[ni][nj] == "#":
        continue

    x, y = ni, nj

    if s[x][y] == "@":
        s[x][y] = "."
        ans += 1

print(x + 1, y + 1, ans)
