#!/usr/bin/env sh

./env.py

docker-compose up --remove-orphans --build -d --scale php-fpm=3 --scale mysql=1 --scale php_cli_worker=3 --scale redis=2

cp ./www/index.php ../www/

cat .env
