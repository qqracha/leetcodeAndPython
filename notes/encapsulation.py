class Router:
    # Инициализируем параметры объекта: name и specs.
    # self — ссылка на конкретный объект этого класса.
    def __init__(self, name, specs):
        self.__name = name        # Приватные атрибуты
        self.__specs = specs

    # Приватные методы
    def __model(self):
        return f"Router model: {self.__name}"

    def __speed(self):
        return f"Router speed: {self.__specs}"

    # Публичный метод для вывода полной информации
    def hard_specs(self):
        return f"{self.__model()}\n{self.__speed()}"

    # __ str__ - магический метод, который показывает, как объект класса будет представлен в виде строки 
    # (например, как ниже после инициализации класса и дальнейшего принта) 
    def __str__(self):
        return f"Router: {self.__name}\nSpecs: {self.__specs}"


r = Router("TP-Link", "1 tb/s")

print(f"__str__ output:\n{r}\n----------------------------") # без __str__ будет: <__main__.router object at 0x74d4076c6780>

# Прямой вызов приватного метода вызовет ошибку 
# r.__model()  # AttributeError

print(f"Encapsulation (via public method):\n{r.hard_specs()}\n")
