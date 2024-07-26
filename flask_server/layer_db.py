# Этот слой отвечает за хранение данных
# Вместо этого уровня может быть SQL база данных
# ни за что не отвечает кроме записи и чтения. Все проблемы выводятся в виде ошибок

import model



class DataBaseExcaption(Exception):
    pass





class LocalStorage:

    def __init__(self):
        self._storage = {}
        self._freed_id_list = []
        self._id_counter = 0


    def create(self, event : model.Event) -> str:
        if not self._freed_id_list:
            event.id = str(self._id_counter)
            self._id_counter += 1
        else:
            _min_val = min(self._freed_id_list)
            event.id = str(_min_val)
            self._freed_id_list.remove(_min_val)
        self._storage[event.id] = event
        return event.id

    def list(self):
        # return self._storage.values()
        return [str(x) for x in self._storage.values()]
        # return self._storage.values()


    def read(self, _id : str):
        if _id not in self._storage:
            raise DataBaseExcaption(f"{_id} not found in storage")
        return self._storage[_id]

    def update(self, _id : str, event : model.Event):
        if _id not in self._storage:
            raise DataBaseExcaption(f"{_id} not found in storage")
        event.id = _id
        self._storage[event.id] = event

    def delete(self, _id : str):
        if _id not in self._storage:
            raise DataBaseExcaption(f"{_id} not found in storage")
        del self._storage[_id]
        self._freed_id_list.append(int(_id))