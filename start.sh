#!/usr/bin/env sh

./env.py

docker-compose build 

docker-compose up -d --scale php-fpm=3 --scale mysql=2 --scale php_cli_worker=3

cp ./www/index.php ../www/

cat .env
