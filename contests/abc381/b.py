s = input()

s_split = s.split("|")

ans = []
for s in s_split[1:-1]:
    a = s.count("-")
    ans.append(a)

print(*ans)
