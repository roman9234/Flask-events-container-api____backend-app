# Модель представляет на объект для обмена данными между разными слоями
class Event:
    id: str
    date: str  # ГГГГ-ММ-ДД
    title: str
    text: str

    # Для тестов: вывод в строке
    # def __str__(self):
    #     return f"{self.id}|{self.date}|{self.title}|{self.text}"
