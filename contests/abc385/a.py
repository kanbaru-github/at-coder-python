a, b, c = map(int, input().split())

ans = "No"
if a == b == c or a + b == c or b + c == a or c + a == b:
    ans = "Yes"

print(ans)
