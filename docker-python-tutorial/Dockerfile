# Python 3.11をベースイメージとして使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt .

# 必要なライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY main.py .

# コンテナ起動時のデフォルトコマンド
# CMD ["python", "main.py"]
