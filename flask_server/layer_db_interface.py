# Этот слой отвечает за взаимодействие с базой данных приложения
# отвечает за контроль id, наличия, отсутсвия заметок


import model
import layer_db


class DataBaseInterfaceExcaption(Exception):
    pass


class DataBaseAPI:
    def __init__(self):
        self._db = layer_db.LocalStorage()
