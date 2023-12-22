
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
#!/bin/bash
# Настройки базы данных
DB_NAME=bux_3_0
DB_HOST=192.168.1.35
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
 
# Настройки бэкапа
BACKUP_DIR=/tmp
DATE=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE=$BACKUP_DIR/$DB_NAME-$DATE.dump
 
# Создание директории для бэкапа, если она не существует
if [ ! -d $BACKUP_DIR ]; then
  mkdir -p $BACKUP_DIR
fi
 
# Создание бэкапа базы данных
pg_dump --format=custom --dbname=postgresql://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME --file=$BACKUP_FILE
 
# Удаление старых бэкапов (оставляем только последние 7 дней)
find $BACKUP_DIR -name "$DB_NAME-*.dump" -mtime +7 -delete