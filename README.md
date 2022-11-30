ЗАПУСК: 

1. sudo vim etc/hosts и вставьте туда следующее:
   192.168.220.2   ipfrontend 
   192.168.220.3   backend 
   192.168.220.5   servicedb 
   192.168.220.6   adminer 
   192.168.220.10  rabbitmq 
   192.168.220.11  celery 
2. docker-compose up --build 

.env файлы в каждом сервисе не заигнорены намеренно для упрощения проверки
