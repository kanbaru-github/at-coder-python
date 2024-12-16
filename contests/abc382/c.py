n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_val = max(b)
ans = [-1 for _ in range(max_val + 1)]

for i in range(n):
    while a[i] <= max_val:
        ans[max_val] = i + 1
        max_val -= 1

for i in range(m):
    print(ans[b[i]])
