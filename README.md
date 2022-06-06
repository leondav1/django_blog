# Django Blog + Rest api

## Setup

Первое, что нужно сделать, это клонироать репозиторий:
```angular2html
$ https://github.com/leondav1/django_blog.git
$ cd django_blog
```
Создайте виртуальную среду для установки зависимостей и активируйте ее:
```angular2html
$ python -m venv env
$ source env/bin/activate
```
Затем установите зависимости:
```angular2html
(env)$ pip install -r requirements.txt
```
Теперь необходимо настроить базу данных.
#### Если вы хотите использовать sqlite3, то сктпируйте следующий код:
```angular2html
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
и вставьте его вместо строки:
```angular2html
DATABASES = {'default': env.db('DATABASE_URL')}
```
Создайте файл .env, добавьте одну настройку DEBUG=True и переходите к пункту создания миграций:
```angular2html
touch .env
sudo nano .env
DEBUG=True
```
#### Настройка базы PostgreSQL.
Установите базу данных PostgreSQL, если её у вас ещё нет.
1. Откройте консоль PostgreSQL
```angular2html
sudo -u postgres psql postgres
```
2. Затем задайте пароль администратора БД
```angular2html
\password postgres
```
3. Далее необходимо создать и настроить пользователя, при помощи которого будем соединяться с БД. Ну и также укажем значения по умолчанию для кодировки, уровня изоляции транзакции и временного пояса
```angular2html
create user <имя пользователя> with password '<пароль>';
alter role <имя пользователя> set client_encoding to 'utf8';
alter role <имя пользователя> set default_transaction_isolation to 'read committed';
alter role <имя пользователя> set timezone to 'UTC';
```
Временное поле можете указать своё, согласно файла settings.py.
4. Создайте базу для проекта и выйти из консоли
```angular2html
create database <имя БД> owner <имя пользователя>;
\q
```
5. И последнее, необходимо настроить раздел DATABASES конфигурационного файла проекта settings.py
Нам понадобится файл .env. Создадим его в консоли и добавим пару настроек.
В DATABASE_URL укажем настройки для подключения к БД:
```angular2html
touch .env
sudo nano .env
DEBUG=True
DATABASE_URL=psql://<имя пользователя>:password@127.0.0.1:5432/<имя БД>?sslmode=require
```
Осталось создать и применить миграции:
```angular2html
python manage.py makemigrations
python manage.py migrate
```
Создаём суперпользователя:
```angular2html
python manage.py createsuperuser
```
Запускаем сервер:
```angular2html
python manage.py runserver
```
Откроем страницу по адресу: http://127.0.0.1:8000/posts/

По следующим ссылкам доступна документация по api
```angular2html
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```

### Немного об API
Создание поста:
```angular2html
http://127.0.0.1:8000/api/post/create/
```
Создание комментария к посту:
```angular2html
http://127.0.0.1:8000/api/comment/create/
```
Вывести список комментариев вплоть до 3-его уровня вложенности:
```angular2html
http://127.0.0.1:8000/api/comments/list/
```
Вывести список коментариев с 3-его уровня и далее:
```angular2html
http://127.0.0.1:8000/api/comments/list/level/
```
