# Object-Oriented Programming

!!! danger "GPT ALERT!!!"
    Эта страница была сгенерирована и ещё не была отредактирована. Качество содержания под вопросом!

## Определение
!!! info ""
    **ООП (Object-Oriented Programming)** — это парадигма программирования, в которой программа строится вокруг **объектов** (данные + поведение), а не вокруг “голых” функций и структур данных.
    Класс в таком подходе служит “шаблоном”, по которому создаются объекты (экземпляры).

## Как это работает
ООП опирается на несколько базовых сущностей:

- <span class="badge">Class</span> (класс) — описание типа: какие данные и методы будут у объектов. 
- <span class="badge">Object</span> (объект) — конкретный экземпляр класса. 
- <span class="badge">Attribute</span> (атрибут/поле) — данные объекта.
- <span class="badge">Method</span> (метод) — функция, “живущая” в классе и работающая с данными объекта. 

Обычно “ядро” ООП объясняют через 4 принципа:  
- [Encapsulation](./encapsulation.md){:.link-accent}  
- [Inheritance](./inheritance.md){:.link-accent}  
- [Polymorphism](./polymorphism.md){:.link-accent}  
- [Abstraction](./abstraction.md){:.link-accent}

## Пример
!!! note "Пример:"
    Минимальный пример класса и объекта в Python: создаём класс, инициализируем объект, вызываем методы. 

        :::python
        class BankAccount:
            def __init__(self, owner: str, balance: int = 0):
                self.owner = owner
                self.balance = balance

            def deposit(self, amount: int) -> None:
                self.balance += amount

            def withdraw(self, amount: int) -> None:
                if amount > self.balance:
                    raise ValueError("Not enough money")
                self.balance -= amount

        # Object (instance)
        acc = BankAccount("Alice", 100)

        acc.deposit(50)
        acc.withdraw(30)

        print(acc.owner, acc.balance)  # Alice 120

!!! info ""
    В этом примере объект `acc` хранит состояние (`owner`, `balance`) и умеет выполнять действия (методы `deposit`, `withdraw`) — это и есть базовая идея ООП. 
