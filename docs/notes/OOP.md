# OOP

## Определение
!!! info ""
    **ООП (Object-Oriented Programming)** — методология программирования, в которой система строится вокруг объектов (данные + поведение), где каждый объект является экземпляром определенного класса, а классы образуют иерархию [наследования](./inheritance.md){:.link-accent}.

## Как это работает
ООП опирается на несколько базовых сущностей:

- <span class="badge">Class</span> — языковая конструкция, определяющий структуру (атрибуты) и поведение (методы) для создаваемых на его основе объектов.

- <span class="badge">Attribute</span> — переменная, принадлежащая экземпляру или классу и содержащая данные, описывающие его состояние. <span class="badge">self.name = name</span>

- <span class="badge">Method</span> — функция, объявленная в составе класса, которая вызывается у объекта (через self) и работает с его данными/атрибутами. <span class="badge">def meow(self):</span>

- <span class="badge">Object</span> — конкретный экземпляр класса со своими значениями атрибутов и возможностью вызывать методы класса.

4 основных принципа ООП:  
- Инкапсуляция ([Encapsulation](./encapsulation.md){:.link-accent})  
- Наследование ([Inheritance](./inheritance.md){:.link-accent})  
- Полиморфизм ([Polymorphism](./polymorphism.md){:.link-accent})  
- Абстракция ([Abstraction](./abstraction.md){:.link-accent})

## Пример
```python
    class Cat:
        def __init__(self, name, color):
            self.name = name      # Attribute | Данные объекта
            self.color = color

        def meow(self):           # Method | Поведение объекта
            return f"{self.name}: meow!"

    cat_object = Cat("Kitty", "black")  # Object | Экземпляр класса
    print(cat_object.name)              # Доступ к атрибуту
    print(cat_object.meow())            # Вызов метода
```