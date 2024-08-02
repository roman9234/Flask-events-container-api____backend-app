# Этот слой отвечает за бизнес-логику приложения
# Этот уровень проверяет, соответствуют ли заметки заданным условиям

from typing import List
import model
import layer_db_interface
from datetime import datetime

from settings import TITLE_LIMIT, TEXT_LIMIT, TIME_FORMAT


class LogicException(Exception):
    pass


class LogicHandler:
    def __init__(self):
        try:
            self._db_interface = layer_db_interface.DataBaseAPI()
        except Exception as e:
            raise LogicException(f"Failed Logic Initialisation : {e}")

    def _validate_event(self, _event: model.Event):
        if _event is None:
            raise LogicException("note is None")
        if _event.date is None:
            raise LogicException("Date is None")
        try:
            datetime.strptime(_event.date, TIME_FORMAT)
        except Exception as e:
            raise LogicException(
                f"Failed to transform {_event.date} into date using format {TIME_FORMAT}, Exception occured : {e}")
        if self._contains_date(_event.date):
            raise LogicException(f"Failed to add new event, as event with date {_event.date} already exists")
        if _event.title is None or len(_event.title) > TITLE_LIMIT:
            raise LogicException(f"title lenght > MAX: {TITLE_LIMIT}")
        if _event.text is None or len(_event.text) > TEXT_LIMIT:
            raise LogicException(f"text lenght > MAX: {TEXT_LIMIT}")

    def _contains_date(self, _str: str) -> bool:
        _event_list = self._db_interface.list()
        for _event in _event_list:
            _date = _event.date
            if _str == _date:
                return True
        return False

    def create(self, _event: model.Event) -> str:
        try:
            self._validate_event(_event)
            return self._db_interface.create(_event)
        except Exception as e:
            raise LogicException(f"Failed Create operation : {e}")

    def list(self) -> List[model.Event]:
        try:
            return self._db_interface.list()
        except Exception as e:
            raise LogicException(f"Failed List operation : {e}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._db_interface.read(_id)
        except Exception as e:
            raise LogicException(f"Failed Read operation : {e}")

    def update(self, _id: str, _event: model.Event):
        try:
            self._validate_event(_event)
            self._db_interface.update(_id, _event)
        except Exception as e:
            raise LogicException(f"Failed Update operation : {e}")

    def delete(self, _id):
        try:
            self._db_interface.delete(_id)
        except Exception as e:
            raise LogicException(f"Failed Delete operation : {e}")

    # для тестов - вывод значений в виде строк
    # def str_list(self) -> List[str]:
    #     try:
    #         return self._db_interface.str_list()
    #     except Exception as e:
    #         raise LogicException(f"Failed List operation : {e}")
