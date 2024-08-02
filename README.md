# Guide-notes-service-flask

Команда запуска Flask-сервера 
(с использованием виртуального окружения)

./venv/Scripts/flask --app ./flask_server/server.py run

Сервис запускается на 
http://127.0.0.1:5000/
Путь API:
http://127.0.0.1:5000/api/v1/calendar/

Формат данных ГГГГ-ММ-ДД 

минимальное интеграционное тестирование 
Можно копировать и вводить в терминал, в том числе по несколько строчек сразу. Терминал понимает Enter в конце строк
Этапы с пометкой (ошибка) выполнять не обязательно, так как они не влияют на данные, а демонстрируют отлов ошибок

Начало тестирования

Выводим список событий (в любой момент тестирования)

curl http://127.0.0.1:5000/api/v1/calendar/ -X GET

1. добавляем события

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "23|2011-02-23|Event 1|SMTHNG HAPPENED!!!"

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "23|2020-10-03|Event 2|SMTHNG ELSE HAPPENED!!!"

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "23|2003-11-09|Event 3|SMTHNG HAPPENED IN 2003!!!1!"


2. Вводим неправильный формат события (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "23|2011-02-23|Event 1|SMTHNG HAPPENED!!!|Hello Exception"


3. Вводим неправильный формат даты (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "42|2002-13-24|Event ERR|SMTHNG STRANGE HAPPENED!!!"

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "42|2002-10-48|Event ERR|SMTHNG STRANGE HAPPENED!!!"

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "42|24-10-2002|Event ERR|SMTHNG STRANGE HAPPENED!!!"

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "42|2002|Event ERR|SMTHNG STRANGE HAPPENED!!!"


4. Не вводим id

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2077-01-01|Event 4|SMTHNG will HAPPEN!!!1!"


5. Вводим дату, совпадающую с другим событием (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2077-01-01|Event 42|SMTHNG will also HAPPEN!!!1!"


6. Вводим слишком длинный заголовок (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2120-03-09|Event 120Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.|SMTHNG will HAPPEN!!!1!"


7. Вводим слишком длинный текст (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2120-03-09|Event 120|Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


8. Обновляем событие

curl http://127.0.0.1:5000/api/v1/calendar/3/ -X PUT -d "2077-03-09|Event 5|SMTHNG will HAPPEN!!!1!"


9. Удаляем событие id 1

curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE


10. Обновляем несуществующее событие (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2007-03-13|Event 1|SMTHNG HAPPENED!!"


11. Неправильный формат при обновлении события (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/2/ -X PUT -d "2007-03-13|Event 1|SMTHNG HAPPENED!!|Bruh"

curl http://127.0.0.1:5000/api/v1/calendar/2/ -X PUT -d "2007-13-13|Event 1|SMTHNG HAPPENED!!"

curl http://127.0.0.1:5000/api/v1/calendar/2/ -X PUT -d "2007-10-23562|Event 1|SMTHNG HAPPENED!!"


12. Добавляем событие не незанятие id 1

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "233|2010-03-21|Event 1|SMTHNG 1 HAPPENED!!!"


13. Обновляем событие так, чтобы даты совпадали с другим событием (ошибка)

curl http://127.0.0.1:5000/api/v1/calendar/3/ -X PUT -d "2010-03-21|Event 4 but date of event 1|SMTHNG HAPPENED!!"



Конец тестирования

Документация

curl - это клиент, который умеет отправлять запросы по адресам и получать HTTP-ответ
Пример:
curl https://www.google.ru/
Выбор метода
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST
curl http://127.0.0.1:5000/api/v1/calendar/ -X GET
Добавление тела запроса
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "request body"

Сервис состоит из нескольких уровней:

API - отлавливает ошибки связанные с форматом данных, полученным в запросах.
Бизнес-логика - отлавливает ошибки при выборе даты события, длины заголовка и текста
интерфейс базы данных - отвечает за взаимодействие с БД. Отлавливает ошибки при записи и чтении
База данных - отвечает за хранение данных

Сервис содержит файлы:
settings.py - содержит настройки приложения
server.py - используется для запуска сервиса
tests.py - используется при отладке уровней API
model.py - модель данных. Не содержит функионала

flask_api_functions_example.py - пример API на фласк. Не связан с сервисом.


Проект содержит примеры кода:
Flask - API
curl - Тестирование
DateTime форматирование str
Exceptions classes
static method
перезагрузка модуля
перевод класса в str
