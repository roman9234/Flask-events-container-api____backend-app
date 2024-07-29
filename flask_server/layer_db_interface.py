# Этот слой отвечает за взаимодействие с базой данных приложения
# отвечает за контроль id, наличия, отсутсвия заметок

from typing import List
import model
import layer_db


class DataBaseInterfaceExcaption(Exception):
    pass


class DataBaseAPI:

    def __init__(self):
        try:
            self._db = layer_db.LocalStorage()
        except Exception as e:
            raise DataBaseInterfaceExcaption(f"Failed DB Initialisation : {e}")

    def create(self, _event: model.Event) -> str:
        try:
            return self._db.create(_event)
        except Exception as e:
            raise DataBaseInterfaceExcaption(f"Failed Create operation : {e}")

    def list(self) -> List[model.Event]:
        try:
            return self._db.list()
        except Exception as e:
            raise DataBaseInterfaceExcaption(f"Failed List operation : {e}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._db.read(_id)
        except Exception as e:
            raise DataBaseInterfaceExcaption(f"Failed Read operation : {e}")

    def update(self, _id: str, _event: model.Event):
        try:
            self._db.update(_id, _event)
        except Exception as e:
            raise DataBaseInterfaceExcaption(f"Failed Update operation : {e}")

    def delete(self, _id):
        try:
            self._db.delete(_id)
        except Exception as e:
            raise DataBaseInterfaceExcaption(f"Failed Delete operation : {e}")

    # для тестов - вывод значений в виде строк
    def str_list(self) -> List[str]:
        try:
            return self._db.str_list()
        except Exception as e:
            raise DataBaseInterfaceExcaption(f"Failed List operation : {e}")