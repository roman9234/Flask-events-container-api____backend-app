# Guide-notes-service-flask

Стек:
Flask - API
curl - Тестирование
DateTime
Exceptions classes
static method


Команда запуска Flask-сервера 
(с использованием виртуального окружения)
./venv/Scripts/flask --app ./flask_server/server.py run

Сервис запускается на 
http://127.0.0.1:5000/

минимальное интеграционное тестирование 
curl http://127.0.0.1:5000/




curl - это клиент, который умеет отправлять запросы по адресам и получать HTTP-ответ
Пример:
curl https://www.google.ru/
Выбор метода
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST
curl http://127.0.0.1:5000/api/v1/calendar/ -X GET
Добавление тела запроса
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "request body"

Мы формально ещё не знаем json так что формат заметок следующий:

Для ещё не созданных заметок
id заголовок текст
1|title|text

Для изменения уже созданной заметки
title|text

Функцию конвертации из текста в модель мы кладём в API

Хранилище
Интерфейс БД




