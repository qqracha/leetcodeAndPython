"""
Метод title() преобразует первую букву каждого слова в заглавную, а остальные — в строчные
"""

text = 'Hello world'

x = text.lower()[::-1].title()

print(x) # Dlrow Olleh