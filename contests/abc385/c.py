# 入力を受け取る（5問の配点）
n = 5
a = list(map(int, input().split()))

# 参加者の得点とその名前を格納するリスト
ranking = []

# すべての問題の組み合わせを試す（1～31の2進数表現を利用）
for s in range(1, 32):  # 1から31まで
    name = ""
    score = 0

    # 各桁（各問題）について判定
    for i in range(n):
        # その問題を解いているかビット演算で判定
        if (s >> i) & 1:
            score += a[i]  # 点数を加算
            name += chr(ord("A") + i)  # 問題名（A,B,C,D,E）を追加

    # 得点の降順でソートするため、scoreにマイナスをつける
    ranking.append((-score, name))

# スコアの降順（-scoreの昇順）、名前の辞書順でソート
ranking.sort()

# 結果を出力
for score, name in ranking:
    print(name)
