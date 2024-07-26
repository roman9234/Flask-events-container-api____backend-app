from flask import Flask, request



app = Flask(__name__)

# спикер предложил всегда добавлять версию API
# чтобы упрощать будущие миграции
API_ROOT = "/api/v1"
# корень API - используется при вызовах
NOTE_API_ROOT = API_ROOT + "/note"

# Функция конвертации полученных данных в модель
import model

class ApiException(Exception):
    # В нём нет логики. Нужен только для разделения
    pass

# TODO понять почему возвращает данные в бинарном виде
def _from_raw(raw_note: str) -> model.Note:
    parts = raw_note.split("|")
    if len(parts) == 2:
        note = model.Note()
        note.id = None
        note.title = str(parts[0])
        note.text = str(parts[1])
        return note
    elif len(parts) == 3:
        note = model.Note()
        note.id = str(parts[0])
        note.title = str(parts[1])
        note.text = str(parts[2])
        return note
    else:
        # Спикер предлагает для каждого модуля определить свой встроеннный тип исключений
        # Чтобы их можно было ловить на разных уровнях и ловить разные виды ошибок
        # TODO выполнить рекомендацию выше
        raise ApiException(f"invalid RAW note data {raw_note}")


# Проверка данных является частью бизнес=логики
# Здесь мы просто конвертируем данные
def _to_raw(note : model.Note) -> str:

    if note.id is None:
        return f"{note.title}|{note.text}"
    else:
        return f"{note.id}|{note.title}|{note.text}"

# путь - корень
@app.route(NOTE_API_ROOT + "/", methods=["POST"])
def create():
    # 201 - код ответа в HTTP
    # 201 - специфика create
    note = _from_raw(str(request.get_data()))
    return f"create {note.id} / {note.title} / {note.text}", 201

# Проверка:
# curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "2|title of 2|hello world of notes"


# тоже корень, но GET
@app.route(NOTE_API_ROOT + "/", methods=["GET"])
def list():
    return "list", 200


# здесь мы используем встроенную в URL переменную
# добавляем к названию id нижнее подчёркивание
# чтобы не задеть системную переменную id
@app.route(NOTE_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id:str):
    note = model.Note()
    note.id = 23
    note.title = "good title"
    note.text = "hello testing note for BRUUUUH"
    return _to_raw(note), 200


# Метод PUT используется для update по принципу CRUD
# create read urpate delete
@app.route(NOTE_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id:str):
    return "update", 200


@app.route(NOTE_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id:str):
    return "delete", 200

# По сути это вся специфика Flask