# Backend

FastAPI によるバックエンド開発のためのテンプレートです

## 環境構築

### パッケージインストール

```bash
uv sync
```

### 環境変数設定

- `direnv`を使用して`.envrc`ファイルを作成し、必要な環境変数を設定する
```
export PYTHONPATH=$(pwd)
```

### 開発サーバーの立ち上げ

```bash
make dev
```

## Frontendとの連携

- `backend`ディレクトリ配下で以下のコマンドを実行し、Schema・APIクライアントの設定ファイルを生成する
```bash
make gen
```

- `frontend`ディレクトリ配下で以下のコマンドを実行し、Schema・APIクライアントを生成する
```bash
yarn gen
```

```bash
# Swagger UIの確認
# ブラウザで`http://127.0.0.1:8000/docs`にアクセス
```
