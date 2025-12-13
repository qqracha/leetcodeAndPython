## Определение
!!! info ""
    **Декоратор** — это языковая конструкция (механизм), которая позволяет добавлять новый функционал к нашей функции, не видоизменяя саму функцию. 

## Как это работает
Декоратор создаёт <span class="badge">Wrapper</span> (обёртку) вокруг исходной функции:

- Исходная функция передаётся в декоратор как аргумент.
- Декоратор возвращает новую функцию-обёртку (wrapper).
- Обёртка может выполнить код *до* и *после* вызова оригинальной функции.
- При этом сама декорируемая функция остаётся нетронутой — меняется только способ её вызова


Эквивалентная запись декоратора <span class="badge">@empty_deco</span> без [синтаксического сахара](./sugar.md){:.link-accent}:  
<span class="badge">my_func = empty_deco(my_func)</span>

## Пример
!!! note "Пример:"
    Подсчёт времени выполнения функции при помощи `Декоратора`.

        :::python
        from typing import Callable
        import time

        def empty_deco(func):  # Identity decorator
            def wrapper(): # Создание обёртки
                start = time.time()
                res = func()
                end = time.time()
                print(f"Исполнение заняло {end-start}")
            return wrapper

        # Decorator
        @empty_deco
        def my_func():
            time.sleep(0.6)
            return 124

        print(my_func())