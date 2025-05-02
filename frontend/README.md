# Frontend

Next.js によるフロントエンド開発のためのテンプレートです

## 環境構築

### パッケージマネージャーのインストール

- [Volta](https://volta.sh/) を使用して Node.js と Yarn のバージョンを管理する

```bash
volta install node
volta install yarn
```

### パッケージインストール

```bash
yarn
```

### Schema・APIクライアントの生成

```bash
cd ../backend
uv run python openapi.py > openapi.json
cd ../frontend
yarn gen
```

### ESLint

- 加えたいルールを`eslint.config.mjs`に記載する

### 環境変数

- 必要な環境変数を`.env.local`に記載する
```
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

### 開発サーバーの立ち上げ

```bash
yarn dev
```
