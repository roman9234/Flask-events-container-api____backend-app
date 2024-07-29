# Этот слой отвечает за бизнес-логику приложения
# Этот уровень проверяет, соответствуют ли заметки заданным условиям

from typing import List
import model
import layer_db_interface

from server import TITLE_LIMIT, TEXT_LIMIT


class LogicExcaption(Exception):
    pass


class LogicHandler:
    def __init__(self):
        try:
            self._db_interface = layer_db_interface.DataBaseAPI()
        except Exception as e:
            raise LogicExcaption(f"Failed Logic Initialisation : {e}")

    @staticmethod
    def _validate_event(_event: model.Event):
        if _event is None:
            raise LogicExcaption("note is None")
        if _event.date is None:
            # TODO добавить проверку формата времени
            raise LogicExcaption(f"title lenght > MAX: {TITLE_LIMIT}")
        if _event.title is None or len(_event.title) > TITLE_LIMIT:
            raise LogicExcaption(f"title lenght > MAX: {TITLE_LIMIT}")
        if _event.text is None or len(_event.text) > TEXT_LIMIT:
            raise LogicExcaption(f"text lenght > MAX: {TEXT_LIMIT}")

    def create(self, _event: model.Event) -> str:
        try:
            # TODO проверка событий одного дня
            return self._db_interface.create(_event)
        except Exception as e:
            raise LogicExcaption(f"Failed Create operation : {e}")

    def list(self) -> List[model.Event]:
        try:
            return self._db_interface.list()
        except Exception as e:
            raise LogicExcaption(f"Failed List operation : {e}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._db_interface.read(_id)
        except Exception as e:
            raise LogicExcaption(f"Failed Read operation : {e}")

    def update(self, _id: str, _event: model.Event):
        try:
            # TODO проверка событий одного дня
            self._db_interface.update(_id, _event)
        except Exception as e:
            raise LogicExcaption(f"Failed Update operation : {e}")

    def delete(self, _id):
        try:
            self._db_interface.delete(_id)
        except Exception as e:
            raise LogicExcaption(f"Failed Delete operation : {e}")

    # для тестов - вывод значений в виде строк
    def str_list(self) -> List[str]:
        try:
            return self._db_interface.str_list()
        except Exception as e:
            raise LogicExcaption(f"Failed List operation : {e}")
