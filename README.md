# Guide-notes-service-flask

Стек:
Flask; curl


Команда запуска Flask-сервера (с использованием виртуального окружения)
./venv/Scripts/flask --app ./flask_server/server.py run

Сервис запускается на 
http://127.0.0.1:5000/api/

минимальное интеграционное тестирование
curl http://127.0.0.1:5000/api/




curl - это клиент, который умеет отправлять запросы по адресам и получать HTTP-ответ
Пример:
curl https://www.google.ru/
Выбор метода
curl http://127.0.0.1:5000/login/user -Method POST