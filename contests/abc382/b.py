n, d = map(int, input().split())
s = list(input())

s.reverse()
cnt = 0

for i in range(n):
    if s[i] == "@":
        s[i] = "."
        cnt += 1
    if cnt == d:
        break

s.reverse()
print(''.join(s))
