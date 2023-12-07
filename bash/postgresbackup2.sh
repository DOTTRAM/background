# Настройки базы данных
DB_NAME=bux_3_0
DB_HOST=192.168.1.35
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
 
# Настройки восстановления
RESTORE_DIR=/tmp
LATEST_BACKUP=$(ls -t $RESTORE_DIR/$DB_NAME-*.dump | head -1)
 
# Проверка наличия бэкапа
if [ -z "$LATEST_BACKUP" ]; then
  echo "Нет доступных бэкапов для восстановления."
  exit 1
fi
 
# Восстановление базы данных с перезаписью
pg_restore --dbname=postgresql://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME --clean $LATEST_BACKUP
 
# Подтверждение восстановления
echo "База данных '$DB_NAME' успешно восстановлена с перезаписью из бэкапа '$LATEST_BACKUP'."