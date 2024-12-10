N = int(input())
S = input()


if N % 2 == 0:
    print("No")
    exit()

for i in range(((N + 1) // 2) - 1):
    if S[i] != "1":
        print("No")
        exit()

if S[((N + 1) // 2) - 1] != "/":
    print("No")
    exit()

for i in range((N + 1) // 2, N):
    if S[i] != "2":
        print("No")
        exit()

print("Yes")
