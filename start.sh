#!/bin/sh

docker-compose up --remove-orphans --build -d --scale php-fpm=1 --scale mysql=1 --scale php_cli_worker=1 --scale redis=1

cp ./www/index.php ../www/

cat .env
