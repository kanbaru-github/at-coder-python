from collections import deque

# 入力を受け取る
h, w, D = map(int, input().split())
s = [input() for _ in range(h)]

# 定数と初期設定
INF = 10**9
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

# 距離を保持するリストの初期化
dist = [[INF] * w for _ in range(h)]

# キューの初期化
q = deque()

# 'H'の位置を探し、距離を0に設定してキューに追加
for i in range(h):
    for j in range(w):
        if s[i][j] == "H":
            dist[i][j] = 0
            q.append((i, j))

# BFS（幅優先探索）
while q:
    i, j = q.popleft()
    d = dist[i][j]

    # 4方向に探索
    for v in range(4):
        ni, nj = i + di[v], j + dj[v]

        # 範囲外チェック
        if ni < 0 or nj < 0 or ni >= h or nj >= w:
            continue

        # 壁チェック
        if s[ni][nj] == "#":
            continue

        # すでに訪問済みチェック
        if dist[ni][nj] != INF:
            continue

        # 距離を更新してキューに追加
        dist[ni][nj] = d + 1
        q.append((ni, nj))

# D以下の距離の座標をカウント
ans = sum(1 for i in range(h) for j in range(w) if dist[i][j] <= D)

# 結果を出力
print(ans)
