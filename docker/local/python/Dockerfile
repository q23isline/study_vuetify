FROM python:3.13
WORKDIR /backend

# GitHub Actions の動作確認用のコミットのためのコメント

# タイムゾーンを日本にする
ENV TZ=Asia/Tokyo

# パイプラインのどれかのコマンドが失敗したらエラーになるように設定する
# https://github.com/hadolint/hadolint/wiki/DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# バージョン依存管理をインストール
# https://github.com/astral-sh/uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin/:$PATH"

# uv を最新バージョンに更新する
RUN uv self update
