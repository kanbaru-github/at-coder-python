# ベースイメージとして PyPy の公式イメージを使用
FROM pypy:3.10-7.3.12

# 必要に応じて追加のツールやライブラリをインストール
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && apt-get clean

# 作業ディレクトリを設定
WORKDIR /workspace

# デフォルトでPythonが使えるように設定
CMD [ "pypy3" ]
