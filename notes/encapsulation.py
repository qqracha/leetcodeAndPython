class Router:
    # Инициализируем параметры объекта: name и specs.
    # self — ссылка на конкретный объект этого класса.
    def __init__(self, name, specs):
        self.name = name
        self.specs = specs 

    def model(self):
        print(f"Router model: {self.name}")

    def hard_specs(self):
        print(f"Router specs: {self.specs}")

    # __ str__ - магический метод, который показывает, как объект класса будет представлен в виде строки 
    # (например, как ниже после инициализации класса и дальнейшего принта) 
    def __str__(self): 
        return f"Router: {self.name}\nSpecs: {self.specs}"

r = Router("TP-link", "1 tb/s")
print(r) # без __str__ будет: <__main__.router object at 0x74d4076c6780>
r.hard_specs()