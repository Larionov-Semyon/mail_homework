## Домашняя работа №3 (Основы HTTP)

###### Установка NGINX
```bash
sudo apt update
sudo apt install nginx
```

###### Настройка брандмауэра
```bash
sudo ufw app list
```
Output:
```
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```

###### Для активации можно ввести следующую команду:
```bash
sudo ufw allow 'Nginx HTTP'
```

###### Для проверки изменений введите:
```bash
sudo ufw status
```
Output:
```
Output
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere                  
Nginx HTTP                 ALLOW       Anywhere                  
OpenSSH (v6)               ALLOW       Anywhere (v6)             
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
```

###### Проверка веб-сервера
```bash
systemctl status nginx
```
Output:
```
nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2020-04-20 16:08:19 UTC; 3 days ago
     Docs: man:nginx(8)
 Main PID: 2369 (nginx)
    Tasks: 2 (limit: 1153)
   Memory: 3.5M
   CGroup: /system.slice/nginx.service
           ├─2369 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─2380 nginx: worker process
```

Вывод подтвердили, что служба успешно запущена. Однако лучше всего протестировать ее запуск посредством запроса страницы из Nginx.

Откройте страницу Nginx по умолчанию, чтобы подтвердить работу программного обеспечения через IP-адрес вашего сервера. Если вы не знаете IP-адрес вашего сервера, вы можете найти его с помощью инструмента icanhazip.com, который выдаст вам ваш публичный IP-адрес, полученный от другого расположения в Интернете:

```bash
curl -4 icanhazip.com
```

или можно использовать команду
```bash
ifconfig
```

Перейдя вы должны получить страницу:

## Welcome to NGINX!

###### Управление процессом Nginx

```bash
#stop
sudo systemctl stop nginx
#start
sudo systemctl start nginx
# restart
sudo systemctl restart nginx
# перезагрузка без отключения соединения
sudo systemctl reload nginx
```