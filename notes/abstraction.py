"""
Абстракция — это принцип объектно-ориентированного программирования, 
который позволяет скрыть детали реализации и предоставить только необходимый интерфейс для работы с объектом. 
Абстрактный подход помогает выделять существенные характеристики объекта, игнорируя незначительные детали, 
и принуждает подклассы к реализации конкретных методов.

В Python абстракция реализуется с помощью модуля abc (Abstract Base Classes), 
который предоставляет базовый класс ABC и декоратор @abstractmethod.

Абстракция обязует использовать определенные методы при наследовании другими классами.
"""
from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# Конкретная реализация
class Cat(Animal):
    def speak(self):
        return "Мяу"
    
    def move(self):
        return "Кошка идет"

class Dog(Animal):
    def speak(self):
        return "Гав"
    
    def move(self):
        return "Собака бежит"

# Использование
cat = Cat()
print(cat.speak())  # Мяу
print(cat.move())   # Кошка идет
