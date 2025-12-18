class Cat:
    def __init__(self, name, color):
        self.name = name      # attribute (данные объекта)
        self.color = color    # attribute

    def meow(self):           # method (поведение объекта)
        return f"{self.name}: meow!"

cat_object = Cat("Kitty", "black")  # object (экземпляр класса)
print(cat_object.name)              # доступ к атрибуту
print(cat_object.meow())            # вызов метода