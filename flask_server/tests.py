import model
import layer_db

# TODO внести код для обновления модулей (reload)
# TODO протестировать базу данных

_db = layer_db.LocalStorage()

ev1 = model.Event()
ev1.id = "23"
ev1.text = "hello1"

ev2 = model.Event()
ev2.id = "3"
ev2.text = "hello2"

ev3 = model.Event()
ev3.id = "2"
ev3.text = "hello3"




print(_db.create(ev1))
print(_db.list())
# print(_db.read("2"))
print(_db.read("1"))
