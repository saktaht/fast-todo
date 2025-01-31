# dockerの起動コマンドまとめ
docker compose up --build --detach

docker compose down --rmi all -v

# migrationするには
docker exec -it demo-app /bin/bash

cd api

migrationファイルの生成 djangoのmigrateみたいな

alembic revision --autogenerate -m "add columns"

migrationの実行 djangoのmakemigrationsみたいな

alembic upgrade head


# 問題点
psycopg2だと非同期なDBではないから、asyncpgを使いたい