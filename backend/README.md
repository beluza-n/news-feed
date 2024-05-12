## Описание
Тестовое задание на должность бекэнд-разработчика компании Itfox
* API доступно по адресу [news-feed.sytes.net](https://news-feed.sytes.net/api/news/)
* [API документация Redoc](https://news-feed.sytes.net/api/schema/redoc/).
* [API документация Swagger](https://news-feed.sytes.net/api/schema/swagger-ui/).
* Исходный код доступен в [публичном репозитории](git@github.com:beluza-n/news-feed.git)


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

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:beluza-n/news-feed.git
```

```
cd news-feed
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* В Linux/macOS

    ```
    source env/bin/activate
    ```

* В Windows

    ```
    source env/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Создать супер-пользователя (опционально):

```
python manage.py createsuperuser
```

Запустить проект:

```
python manage.py runserver
```

Перейти на url-адрес согласно документации, например, на http://127.0.0.1:8000/api/news
Админ-панель доступна по адресу http://127.0.0.1:8000/admin/