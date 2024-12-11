s = input()
flag = True

if len(s) % 2 == 1:
    flag = False

if flag:
    for i in range(len(s) // 2):
        if s[2 * i] != s[2 * i + 1]:
            flag = False

cnt = [0 for i in range(26)]

if flag:
    for i in range(len(s)):
        cnt[ord(s[i]) - ord("a")] += 1
    for i in range(26):
        if cnt[i] != 0 and cnt[i] != 2:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
