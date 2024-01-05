# Закидываем файл daemon.json в папку /etc/docker/
# открываем порт 9323  "firewall-cmd --permanent --zone=public --add-port=9323/tcp"
# Перезагрузите правила брандмауэра, чтобы применить изменения "firewall-cmd --reload"
# убеждаемся что нужные порты открылись firewall-cmd --list-all
# Перезапускаем docker  "systemctl restart docker
# Закинем файл  prometheus.yml в папку  где мы находимся.
# Отредактируем её. Вместо <PRIVATE_IP_ADDRESS> вбиваем IP адресс машины.
# Закинем файл docker-compose.yml в папку где мы находимся. Отредактируем его. Проверяем Volumes
# Далее создаём демон на автозапуск docker-compose-myappname.service после рестарта сервера.
# Включаем сервис: "sudo systemctl enable docker-compose-myappname"
# После чего запускаем docker-compose.  "docker-compose up -d "
