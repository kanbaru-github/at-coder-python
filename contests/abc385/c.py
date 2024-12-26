n = int(input())
h = list(map(int, input().split()))

ans = 0
for w in range(1, n + 1):  # wは「ビル同士の間隔」を表す
    for si in range(w):  # siは「最初に選ぶビルの位置」を表す
        # 間隔wで、位置siから始めてビルを選んでいく
        a = []
        for i in range(si, n, w):
            a.append(h[i])  # 選んだビルの高さを記録

        # 選んだビルの中で、同じ高さが何棟連続しているかを数える
        val = -1  # 現在注目しているビルの高さ
        length = 0  # 同じ高さのビルが連続している数
        for x in a:
            if val == x:  # 前のビルと同じ高さの場合
                length += 1
            else:  # 異なる高さのビルが出てきた場合
                val = x
                length = 1
            ans = max(ans, length)  # 最大値を更新

print(ans)
