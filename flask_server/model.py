# Модель представляет на объект для обмена данными между разными слоями
class Event:
    id: str
    date: str
    title: str
    text: str

    def __str__(self):
        return f"{self.id}|{self.date}|{self.title}|{self.text}"



# TODO определить метод str чтобы вместо адреса в памяти выводилась заметка
