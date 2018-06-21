# Usage

*使用前请确认安装docker和docker-compose*,如何安装见`常见问题`

*以下配置假定当前目录为包含docker-compose.yml文件的同级目录*

*laravel/lumen请使用master分支,ci请使用ci分支*

## Init 初始化

Run follow command in this dir:
在目录中执行如下指令:

`./init.sh`

## Start 启动

Run follow command in this dir:
在目录中执行如下指令:

`./start.sh`

## Stop 停止

Run follow command in this dir:
在目录中执行如下指令:

`./stop.sh`

## Restart 重启

Run follow command in this dir:
在目录中执行如下指令:

`./restart.sh`


## Port info 端口信息

`cat .env`

# Config 配置

*以下配置假定当前目录为包含docker-compose.yml文件的同级目录*

## nginx

修改`nginx/nginx.conf`中`root`值为对应目录

*注意* `root`中的`/var/www/html`路径对应于当前环境下的`../www`目录

## crontab

Edit `php_cli_crontab/crontab`

## worker

Edit `php_cli_worker/worker.sh`
将要执行的worker启动脚本放入`php_cli_worker/worker.sh`文件
*注意* 脚本中不需要使用`nohup`和`&`将进程放入后台

## php_cli
修改`php_cli/Dockerfile`中的`WORKDIR`值为对应目录
*注意* `root`中的`/var/www/html`路径对应于当前环境下的`../www`目录

# 常见问题

## 如何执行composer install 或其他命令

启动状态下,在当前目录下执行如下命令

`docker-compose ps | grep php_cli`

找到php_cli对应的容器(container)名称,类似`php_docker_env_php_cli_1`

在此容器中执行`composer install`,指令如下

`docker exec php_docker_env_php_cli_1 composer install`

## 如何进入容器(container)调试

找到对应的容器(container)名称,方法见上.执行指令

`docker exec -it php_docker_env_php_cli_1 bash`

## 如何访问mysql和redis

mysql可以通过phpmyadmin访问,端口见上.
程序中访问mysql

`host`:`mysql`
`port`:`3306`
`username`:`root`
`password`:`123456`(默认)

程序中访问redis

`host`:`redis`
`port`:`6379`

*注意*不要使用ip配置或访问,用`hostname`访问,在本项目中使用`mysql`,`redis`,`php_cli`,`nginx`等

## 如何设置开机启动

在`/etc/rc.local`中配置命令

`cd /path/to/this/dir && docker-compose up -d`

## 如何查看日志

查看全部日志

`docker-compose logs`

查看单个容器(container)日志,示例如下

`docker-compose logs mysql`

## 如何安装docker(centos7) 
见`https://docs.docker.com/install/linux/docker-ce/centos/`

## 如何安装docker-compose
`sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose`
