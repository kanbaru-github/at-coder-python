n = int(input())

ans = 0
elapsed = 0

for i in range(n):
    t, v = map(int, input().split())

    ans -= t - elapsed
    if ans < 0:
        ans = 0

    elapsed = t
    ans += v

print(ans)
