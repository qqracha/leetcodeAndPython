# Генератор - вид итератора, который не хранит в себе последовательность данных, а вычисляет каждое следующее значение при помощи формулы

# Пример генератора:
def count_up_to(n):
    print("Generator start!")
    i = 1
    while i <= n: # Пока i меньше или равен n
        yield i # Возвращает значение и "замораживает" функцию
        i += 1
    print("Generator end!")


# Инициализируем генератор
gen = count_up_to(10)

# Получаем значение по одному
for number in gen:
    print(number)

# Пример генератора с .send и возведением в квадрат
def generator_example():
    value = yield #  точка ожидания внешнего значения
    yield value ** 2

gen_e = generator_example()

next(gen_e)
print(gen_e.send(10))

# Пример генератора с ошибкой
def generator_with_exception():
    try:
        yield
    except ValueError:
        yield "Oops.."

gen_error = generator_with_exception()
next(gen_error) # Запускаем оператор до первого yield
print(gen_error.throw(ValueError)) # Выбрасывает исключение внутри генератора

# Пример генератора с методом .close
def generator_with_close():
    try:
        yield 1
    except GeneratorExit:
        print("Generator was ended!")

gen_close = generator_with_close()
next(gen_close)
gen_close.close()