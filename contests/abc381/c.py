N = int(input())
S = input()
ans = 0

for i in range(N):
    if S[i] == "/":
        cnt = 1
        left = i - 1
        right = i + 1

        while left >= 0 and right < N and S[left] == "1" and S[right] == "2":
            cnt += 2
            left -= 1
            right += 1

        ans = max(ans, cnt)

print(ans)
