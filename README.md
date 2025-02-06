# envファイルについて
.env.exampleファイルにテンプレートを書いたので、それを元に.envファイルを作れば動くと思います

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

# test実行方法
docker compose run --entrypoint "poetry run pytest" demo-app

# git pushする前にすること
- migrationしないとバージョンが違うって言われてエラーになる

# 参考にした記事
https://zenn.dev/sh0nk/books/537bb028709ab9

https://qiita.com/nonamenme/items/5a598e90e448285b9bf2#4-4-%E7%94%9F%E6%88%90%E3%81%95%E3%82%8C%E3%82%8Bmigration%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%90%8D%E3%82%92%E5%A4%89%E6%9B%B4%E3%81%99%E3%82%8B