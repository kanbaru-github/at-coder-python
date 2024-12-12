n, d = map(int, input().split())
s = input()

ans = 0
for i in s:
    if i == ".":
        ans += 1
ans += d

print(ans)
