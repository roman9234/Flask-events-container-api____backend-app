import model
# import layer_db
import layer_logic
from importlib import reload

# перезагрузка модуля
layer_logic = reload(layer_logic)

_db = layer_logic.LogicHandler()

ev1 = model.Event()
ev1.id = "23"
ev1.date = "2021-06-13"
ev1.title = "event 2021"
ev1.text = "smtg happened"

ev2 = model.Event()
ev2.id = "221"
ev2.date = "2001-03-20"
ev2.title = "event 2001"
ev2.text = "smtg happened 2001"

ev3 = model.Event()
ev3.id = "18"
ev3.date = "2017-02-27"
ev3.title = "event 2017"
ev3.text = "smtg happened 2017"

ev4 = model.Event()
ev4.id = "1436"
ev4.date = "2005-08-23"
ev4.title = "event 2005"
ev4.text = "smtg happened 2005"

ev5 = model.Event()
ev5.id = "1231"
ev5.date = "2001-03-20"
ev5.title = "event 2019"
ev5.text = "smtg happened 2019"

print(_db.create(ev1))
print(_db.create(ev2))
print(_db.create(ev3))
_db.update("2", ev5)
