#!/usr/bin/env bash

## 启动mysql
ps -ef | grep mysqld
cd /usr/bin ./safe_mysqld &


## 关闭mysql
cd /usr/bin ./mysqladmin -u root -p shutdown


# sae
source /Users/guanghui/Development/pythonsae2/bin/activate
cd /Users/guanghui/MyCloudProjects/exchcard-sae/exchcard
python manage.py runserver



# github
source /Users/guanghui/Development/pythonsae2/bin/activate
cd /Users/guanghui/MyGithub/exchcard
python manage.py runserver









