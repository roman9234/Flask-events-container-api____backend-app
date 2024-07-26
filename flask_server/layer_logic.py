# Этот слой отвечает за бизнес-логику приложения
# Этот уровень проверяет, соответствуют ли заметки заданным условиям


import model
import layer_db_interface


class LogicExcaption(Exception):
    pass


class LogicHandler:
    def __init__(self):
        self._db_interface = layer_db_interface.DataBaseAPI()
