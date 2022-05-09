# Тестовое задание *Junior*

## Веб-сервис

Решение тестового задания компании [Bewise.ai](https://bewise.ai/) с использованием **Django**, **Django REST framework**, **PostgreSQL**, **Docker**, **Docker-compose**.

Само задание приведено ниже.

### Запуск

1. Клонировать проект в пустую папку:
```shell
git clone https://github.com/zelo78/test_task_bewise.git .
```
2. Копировать файл `start.env` как `.env` (Он должен находится в корне проекта, рядом с `README.md`)
```shell
cp start.env .env
```
3. Создать и запустить контейнер (при запуске котейнера будут созданы и применены миграции):
```shell
docker-compose build
docker-compose up -d
``` 
4. Создать суперпользователя:
```shell
docker exec -it app python manage.py createsuperuser --username USER
```

### Примеры запросов

1. Список полученных вопросов (имеющихся в локальной БД)
```shell
curl http://0.0.0.0:8000/api/questions/
```
Получаем список имеющихся вопросов:
```text
{
    "count": 63,
    "next": "http://0.0.0.0:8000/api/questions/?page=2",
    "previous": null,
    "results": [
        {
            "id": 22001,
            "answer": "Rosa Parks",
            "question": "This Montgomery seamstress was thrown off a bus one other time before her famous Dec. 1, 1955 incident",
            "value": 200,
            "airdate": "1998-05-21T16:00:00+04:00",
            "created_at": "2014-02-12T02:58:58.201000+04:00",
            "updated_at": "2014-02-12T02:58:58.201000+04:00",
            "category": {
                "internal_id": 31,
                "id": 2278,
                "title": "black americans",
                "created_at": "2014-02-12T02:58:58.018000+04:00",
                "updated_at": "2014-02-12T02:58:58.018000+04:00",
                "clues_count": 15
            }
        },
        <и так далее>
    ]
}
```

2. Получение вопросов из внешнего сервиса в локальную БД, авторизация с помощью BasicAuthentication 
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"questions_num": 10}' \
  -u USER:PASSWORD \
  http://0.0.0.0:8000/api/questions/
```

3. Получение вопросов из внешнего сервиса в локальную БД, авторизация с помощью JWT
- создаём токен авторизации
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "USER", "password": "PASSWORD"}' \
  http://127.0.0.1:8000/api/token/
```
Получаем ответ вида
> {"refresh":"ey...I0","access":"ey...lQ"}

- авторизуемся с помощью токена:
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ey...lQ" \
  -d '{"questions_num": 10}' \
  http://0.0.0.0:8000/api/questions/
```
Получаем ответ вида (последний ранее полученный вопрос):
> {
    "id": 105357,
    "answer": "doge",
    "question": "Several members of the Dandolo family held this Venetian job",
    "value": 800,
    "airdate": "2011-01-27T15:00:00+03:00",
    "created_at": "2014-02-14T06:12:08.090000+04:00",
    "updated_at": "2014-02-14T06:12:08.090000+04:00",
    "category": {
        "internal_id": 94,
        "id": 14206,
        "title": "in god we trust",
        "created_at": "2014-02-14T06:12:07.105000+04:00",
        "updated_at": "2014-02-14T06:12:07.105000+04:00",
        "clues_count": 5
    }
}

### Реализованные URL

- <http://0.0.0.0:8000/api/questions/> - API для добавления вопросов в базу данных
- <http://0.0.0.0:8000/admin/> - интерфейс администрирования
- <http://0.0.0.0:8000/api/token/> - API авторизации

### Swagger/OpenAPI 2.0 specifications

- <http://0.0.0.0:8000/swagger/> - A swagger-ui view of your API specification 
- <http://0.0.0.0:8000/swagger.json> - A JSON view of your API specification 
- <http://0.0.0.0:8000/swagger.yaml> - A YAML view of your API specification
- <http://0.0.0.0:8000/redoc/> - A ReDoc view of your API specification 

### Авторизация

1. Получение токена
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "USER", "password": "PASSWORD"}' \
  http://0.0.0.0:8000/api/token/
```
2. Авторизация с использованием токена
```shell
curl \
  -H "Authorization: Bearer <token>" \
  http://0.0.0.0:8000/api/questions
```

## Тестовое задание

Тестовое задание компании [Bewise.ai](https://bewise.ai/).

Время выполнения задания оценивается в 4-8 человеко-часов (для специалиста уровня *Junior*). 
Максимальный срок выполнения - неделя с момента отправки кандидату. 

Результат выполнения задания должен быть выложен соискателем в публичный репозиторий github и помимо кода проекта содержать подробные инструкции по сборке и запуску. Ссылку на проект необходимо направить на почту: <try.ai@yandex.ru>, в тексте письма указать ваше ФИО и ссылку на ваше резюме.

## Задачи:

1. С помощью **Docker** (предпочтительно **docker-compose**) развернуть образ с любой опенсорсной СУБД (предпочтительно **PostgreSQL**). Предоставить все необходимые скрипты и конфигурационные (`docker-compose`) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть использовать volume-ы для хранения файлов СУБД на хост-машине).

2. Реализовать на **Python3** простой веб сервис (с помощью **FastAPI** или **Flask**, например), выполняющий следующие функции:
   - В сервисе должно быть реализовано **REST API**, принимающее на вход `POST` запросы с содержимым вида `{"questions_num": integer}`;
   - После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) <https://jservice.io/api/random?count=1> указанное в полученном запросе количество вопросов.
   - Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 
     1. ID вопроса, 
     2. Текст вопроса, 
     3. Текст ответа, 
     4. Дата создания вопроса. 

   - В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
   - Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины, а в случае его отсутствия - пустой объект.

3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.

4. Желательно, если при выполнении задания вы будете использовать **docker-compose**, **SqlAlchemy**, пользоваться аннотацией типов.

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.4
- [Django REST framework](https://www.django-rest-framework.org/) v. 3.13.1
- [Psycopg](https://www.psycopg.org/docs/) v. 2.9.3 - PostgreSQL database adapter for Python
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) v. 1.20.0 - Yet another Swagger generator. Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
 