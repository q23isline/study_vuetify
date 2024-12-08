# study_vuetify

[![LICENSE](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=555555&color=007acc&logoColor=007acc)](https://open.vscode.dev/q23isline/study_vuetify)

[![Python](https://img.shields.io/static/v1?logo=python&label=Python&message=v3.13&labelColor=555555&color=#3776AB&logoColor=#3776AB)](https://www.python.org/)
[![Node.js](https://img.shields.io/static/v1?logo=node.js&label=Node.js&message=v22.12.0&labelColor=555555&color=339933&logoColor=339933)](https://nodejs.org)
[![npm](https://img.shields.io/static/v1?logo=npm&label=npm&message=v10.9.0&labelColor=555555&color=CB3837&logoColor=CB3837)](https://www.npmjs.com/)
[![Vue.js](https://img.shields.io/static/v1?logo=vue.js&label=Vue.js&message=v3.4.31&labelColor=555555&color=4FC08D&logoColor=4FC08D)](https://ja.vuejs.org/)
[![Vuetify](https://img.shields.io/static/v1?logo=vuetify&label=Vuetify&message=v3.7.5&labelColor=555555&color=1867C0&logoColor=1867C0)](https://vuetifyjs.com/ja/)

Vuetify 勉強用リポジトリ

[バックエンド開発ガイドライン](./backend/README.md)
[フロントエンド開発ガイドライン](./frontend/README.md)

## 前提

- インストール（ホスト上に）
  - [Windows Subsystem for Linux](https://learn.microsoft.com/ja-jp/windows/wsl/)
  - [Git](https://git-scm.com/)
  - [Docker Desktop](https://www.docker.com/ja-jp/products/docker-desktop/)
  - [Visual Studio Code](https://code.visualstudio.com/)
- インストール（Windows Subsystem for Linux 上に）
  - [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
  - [Python](https://www.python.org/)

## はじめにやること

1. Windows Subsystem for Linux 上でプログラムダウンロード

    ```bash
    git clone 'https://github.com/q23isline/study_vuetify.git'
    ```

2. リポジトリのカレントディレクトリへ移動

    ```bash
    cd study_vuetify
    ```

3. 開発準備

    ```bash
    cp .vscode/settings.json.default .vscode/settings.json
    ```

4. アプリ立ち上げ

    ```bash
    docker compose build
    docker compose up -d
    # ライブラリインストール
    docker compose exec frontend npm install
    # VSCode でプログラムを変更できるように、Linux 権限の他者・グループ・作成者に読み込み・書き込み権限を与える
    sudo chmod -R ogu+rw frontend

    cd backend
    pip3.13 install -r requirements.txt
    sam local start-api -p 3010 --debug > logs/debug.log 2>&1 --docker-network study_vuetify_default
    ```

## 日常的にやること

### システム起動

```bash
# コンテナ起動
docker compose up -d
# フロントエンド起動
docker compose exec frontend npm run dev -- --host
# バックエンド起動
sam local start-api -p 3010 --debug > logs/debug.log 2>&1 --docker-network study_vuetify_default
```

### システム終了

```bash
# バックエンド起動ターミナルで Ctrl + c
# フロントエンド起動ターミナルで Ctrl + c

docker compose down
```

## 動作確認

### URL

- バックエンド
  - <http://localhost:3010>
- フロントエンド
  - <http://localhost:3000>

## バックエンド静的解析単体実行

```bash
cd backend

# フォーマッター
autopep8 --diff --recursive . --exclude=.aws-sam,tests
black --diff . --exclude='\.aws-sam|tests'

# リンター
pylint ./ --rcfile=.pylintrc --ignore-paths=.aws-sam,tests
flake8 --config=.flake8 --extend-exclude=.aws-sam,tests
mypy ./ --exclude=.aws-sam --exclude=tests
```

## フロントエンド静的解析単体実行

```bash
docker compose exec frontend npm run type-check
docker compose exec frontend npm run lint
```

## Dockerfile コード静的解析実行

```bash
docker run --rm -i hadolint/hadolint < $(pwd)/docker/local/node/Dockerfile
```

## ログ出力場所

| サービス | ログ出力場所  |
| -------- | ------------- |
| Node.js  | logs/frontend |
| Python   | backend/logs  |

## Permission Deniedエラーが出た時の解決方法

```bash
# プロジェクト全体のファイルすべてに読み込み、書き込み権限を与える
sudo chmod -R ogu+rw ./
# インストールしたライブラリに実行権限を含めた全権限を与える
sudo chmod -R 777 frontend/node_modules
```
