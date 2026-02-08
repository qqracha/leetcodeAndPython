# SOLID

!!! note ""
    **SOLID** - мнемоническая аббревиатура, состоящая из пяти принципов, призванных сделать исходный код более понятным, гибким и поддерживаемым.

## Принципы SOLID

<span class="badge">S</span> **Single Responsibility Principle** *[SRP]* — принцип единственной ответственности.  

<span class="badge">O</span> **Open Closed Principle** *[OCP]* — принцип открытости-закрытости.  

<span class="badge">L</span> **Liskov Substitution Principle** *[LSP]* — принцип подстановки Барбары Лисков (Заменяемость объектов на экземпляры).  

<span class="badge">I</span> **Interface Segregation Principle** *[ISP]* — принцип разделения интерфейса.  

<span class="badge">D</span> **Dependency Inversion Principle** *[DIP]* — принцип инверсии зависимостей.  

![solid](https://habrastorage.org/getpro/habr/upload_files/dbc/582/da9/dbc582da9e391cca96f4ad0c978154f7.png)

### **S**, Принцип единственной отвественности [SRP]

!!! note ""
    **Single Responsibility Principle** - Каждый класс должен отвечать только за одну зону ответственности (действий), чтобы его было проще дополнять и менять. Изменение должно минимально затрагивать код. Надо разделять функциональность большого класса на более мелкие части, отвечающие за конкретные задачи.

```python
    class Movement:
        def move(self):
            pass

    class Speaker:
        def speak(self):
            pass

    class Robot:
        def __init__(self):
            self._movement = Movement() 
            self._speaker = Speaker()   
        
        def move(self):
            self._movement.move()
        
        def speak(self):
            self._speaker.speak()
```

### **O**, Принцип Открытости-Закрытости [OCP]

!!! note ""
    **Open Closed Principle** - Класс должен быть закрыт для изменения, но открыт для расширения. Пишем код так, чтобы другие могли легко расширить функционал, не меняя написанный (оттестированный, понравившийся твоему начальнику) код.

```python
    class Character(ABC):
        @abstractmethod
        def display_info(self):
            pass

    class Knight(Character):
        def display_info(self):
            print("Я Рыцарь")

    class Wizard(Character):
        def display_info(self):
            print("Я Маг")

    if __name__ == "__main__":
        character = Knight()
        character.display_info()  # Я Рыцарь
        
        character = Wizard()
        character.display_info()  # Я Маг

```

### **L**, Принцип подстановки Барбары Лисков [LSP]

!!! note ""
    **Liskov Substitution Principle** - Если в коде программы Базовый класс заменить на его Наследника, то программа должна работать, так как в Наследнике есть все операции, которые были в Базовом. В Базовый класс нужно выносить только общую логику, которую наследники будут реализовывать. Наследников создаем только тогда, когда они правильно реализуют логику Базового класса.

```python
    class Bird(ABC):
        @abstractmethod
        def move(self):
            pass

    class FlyingBird(Bird):
        def move(self):
            self.fly()
        
        def fly(self):
            print("Летаю!")

    class Sparrow(FlyingBird):
        def fly(self):
            print("Воробей летит")

    class Penguin(Bird):
        def move(self):
            self.swim()
        
        def swim(self):
            print("Пингвин плывёт")

    def make_bird_move(bird: Bird):
        bird.move()
```

### **I**, Принцип Разделения Интерфейса [ISP]

!!! note ""
    **Interface Segregation Principle** - Клиенты не должны зависеть от интерфейсов, которые они не используют. Большие интерфейсы следует разбивать на интерфейсы поменьше. Так клиенты смогут использовать только те интерфейсы, которые им нужны. Это делает менее связанный код, уменьшает зависимости между элементами системы, упрощает изменения в коде.

```python
    class Movable(ABC):
        @abstractmethod
        def move(self):
            pass

    class Speakable(ABC):
        @abstractmethod
        def speak(self):
            pass

    class Flyable(ABC):
        @abstractmethod
        def fly(self):
            pass

    class Robot(Movable, Speakable):
        def move(self):
            pass
        
        def speak(self):
            pass

    class Drone(Flyable):
        def fly(self):
            pass
```

### **D**, Принцип Инверсии Зависимостей [DIP]

!!! note ""
    **Dependency Inversion Principle** - Зависьте от интерфейсов, а не от конкретных классов. Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций. Интерфейсы не должны зависеть от реализации, а вот реализация должна зависеть от интерфейсов.

```python
    class User:
        pass

    class IDatabase(ABC):
        @abstractmethod
        def save_data(self, user: User):
            pass

    class Database(IDatabase):
        def save_data(self, user: User):
            # Сохранение данных в БД
            pass

    class UserService:
        def __init__(self, database: IDatabase):
            self._database = database
        
        def add_user(self, user: User):
            self._database.save_data(user)
            pass
```

## Источники

Подробнее на: [Одноглазый змей - SOLID](https://speedrunit.ru/question/9/?)