## Описание
Тестовое задание на должность бекэнд-разработчика компании Itfox
* API доступно по адресу [news-feed.sytes.net](https://news-feed.sytes.net/api/news/)
* [API документация Redoc](https://news-feed.sytes.net/api/schema/redoc/).
* [API документация Swagger](https://news-feed.sytes.net/api/schema/swagger-ui/).
* Исходный код доступен в [публичном репозитории](https://github.com/beluza-n/news-feed)


Автор:
* Анастасия Гречкина (Github beluza-n, telegram @beluza_n)


## Стэк:
* Python
* Django Rest Framework
* PostgreSQL
* Docker
* nginx
* Gunicorn


### Как запустить проект:

Клонировать репозиторий и перейти в папку news-feed:

```
git clone git@github.com:beluza-n/news-feed.git
```

```
cd news-feed
```
Создать файл .env на основе .env.example

Запустить локально Docker compose:
```
sudo docker compose up -d
```

Выполнить команды миграции, сбора статических файлов, создания суперпользователя:
```
sudo docker compose exec backend python manage.py migrate
sudo docker compose exec backend python manage.py collectstatic
sudo docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
sudo docker compose exec backend python manage.py createsuperuser
```

Локальный сервер запущен.
Перейти на url-адрес согласно документации, например, на http://127.0.0.1:8000/api/news
Админ-панель доступна по адресу http://127.0.0.1:8000/admin/

Для остановки сервера использовать команду :
```
sudo docker compose down
```
