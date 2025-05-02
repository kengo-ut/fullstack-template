# Fullstack-Template

Next.js と FastAPI によるフルスタック開発のためのテンプレートです (Health Status Checker が含まれています)

## デモ画像

![demo](/assets/health_status_checker.png)

## 環境構築

### backend

1. `backend/.envrc`ファイルを作成し、必要な環境変数を設定する

2. `backend`ディレクトリで以下のコマンドを実行し、依存パッケージをインストールする

   ```bash
   uv sync
   ```

3. `backend`ディレクトリで以下のコマンドを実行し、開発サーバーを立ち上げる
   ```bash
   make dev
   ```

4. `backend`ディレクトリで以下のコマンドを実行し、Schema・APIクライアントの設定ファイルを生成する

   ```bash
   make gen
   ```

### frontend

1. `frontend`で使用する Node.js と Yarn をインストールする

   ```bash
   volta install node
   volta install yarn
   ```

2. `frontend`ディレクトリで以下のコマンドを実行し、依存パッケージをインストールする

   ```bash
   yarn
   ```

3. `frontend`ディレクトリで以下のコマンドを実行し、Schema・API クライアントを生成

   ```bash
   yarn gen
   ```

4. `frontend`ディレクトリで、以下の環境変数ファイル`frontend/.env.local`を作成する

   ```
   NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
   ```

5. `frontend`ディレクトリで以下のコマンドを実行し、開発サーバーを立ち上げる

   ```bash
   yarn dev
   ```

6. [http://localhost:3000](http://localhost:3000)へアクセスしてページが表示されれば OK
