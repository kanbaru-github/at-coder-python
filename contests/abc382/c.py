n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

r = max(b)
ans = [-1 for _ in range(r + 1)]

for i in range(n):
    while a[i] <= r:
        ans[r] = i + 1
        r -= 1

for i in range(m):
    print(ans[b[i]])
