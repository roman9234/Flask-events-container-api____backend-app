from flask import Flask, request

import model
import layer_logic

app = Flask(__name__)
logic = layer_logic.LogicHandler()

# TODO протестировать
# TODO ввести команды для теста в readme и отправить на проверку
# TODO закрыть вопросы по коду
# TODO заполнить readme для себя

# спикер предложил всегда добавлять версию API
# чтобы упрощать будущие миграции
API_ROOT = "/api/v1"
# корень API - используется при вызовах
NOTE_API_ROOT = API_ROOT + "/calendar"

# Функция конвертации полученных данных в модель

class ApiException(Exception):
    # В нём нет логики. Нужен только для разделения
    pass

# TODO понять почему возвращает данные в бинарном виде
def _from_raw(raw_event: str) -> model.Event:
    parts = raw_event.split("|")
    if len(parts) == 3:
        _event = model.Event()
        _event.id = None
        _event.date = str(parts[0])
        _event.title = str(parts[1])
        _event.text = str(parts[2])
        return _event
    elif len(parts) == 4:
        _event = model.Event()
        _event.id = str(parts[0])
        _event.date = str(parts[1])
        _event.title = str(parts[2])
        _event.text = str(parts[2])
        return _event
    else:
        # Спикер предлагает для каждого модуля определить свой встроеннный тип исключений
        # Чтобы их можно было ловить на разных уровнях и ловить разные виды ошибок
        # TODO выполнить рекомендацию выше
        raise ApiException(f"invalid RAW note data {raw_event}")


# Проверка данных является частью бизнес=логики
# Здесь мы просто конвертируем данные
def _to_raw(_event : model.Event) -> str:
    return f"{_event.id}|{_event.date}|{_event.title}|{_event.text}"

# путь - корень
@app.route(NOTE_API_ROOT + "/", methods=["POST"])
def create():
    # 201 - код ответа в HTTP
    # 201 - специфика create
    try:
        _event = _from_raw(str(request.get_data()))
        _new_id = logic.create(_event)
        return f"new event id = {_new_id}", 201
    except Exception as e:
        return f"failed create operation : {e}", 404


# Проверка:
# curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "2|title of 2|hello world of notes"


# тоже корень, но GET
@app.route(NOTE_API_ROOT + "/", methods=["GET"])
def list():
    try:
        _events_list = logic.list()
        return "\n".join([_to_raw(x) for x in _events_list]), 200
    except Exception as e:
        return f"failed list operation : {e}", 404


# здесь мы используем встроенную в URL переменную
# добавляем к названию id нижнее подчёркивание
# чтобы не задеть системную переменную id
@app.route(NOTE_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id:str):
    try:
        return _to_raw(logic.read(_id)), 200
    except Exception as e:
        return f"failed read operation : {e}", 404

# Метод PUT используется для update по принципу CRUD
# create read urpate delete
@app.route(NOTE_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id:str):
    try:
        logic.update(_id)
        return "update", 200
    except Exception as e:
        return f"failed update operation : {e}", 404


@app.route(NOTE_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id:str):
    try:
        logic.delete(_id)
        return "delete", 200
    except Exception as e:
        return f"failed delete operation : {e}", 404

# По сути это вся специфика Flask