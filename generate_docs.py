"""
Скрипт для автоматической генерации документации MkDocs
из Python файлов в папках notes/ и solutions/
"""

from pathlib import Path
import re

# Настройки
ROOT = Path(__file__).parent
NOTES_DIR = ROOT / "notes"
SOLUTIONS_DIR = ROOT / "solutions"
DOCS_DIR = ROOT / "docs"
DOCS_NOTES_DIR = DOCS_DIR / "notes"
DOCS_LEETCODE_DIR = DOCS_DIR / "leetcode"

# Функция для создания красивого заголовка из имени файла
def make_title(filename):
    """
    Преобразует имя файла в читабельный заголовок
    Например: starred_expression.py -> Starred Expression
    """
    name = filename.replace('.py', '')
    # Заменяем underscores на пробелы
    name = name.replace('_', ' ')
    # Делаем заглавными первые буквы
    return name.title()


# Функция для создания .md файла для одного .py
def create_md_for_py(py_file, output_dir, relative_path):
    """
    Создаёт Markdown файл с включением Python исходника

    Args:
        py_file: Path к .py файлу
        output_dir: Path к директории docs/notes/ или docs/leetcode/
        relative_path: относительный путь от корня проекта (для snippets)
    """
    # Имя .md файла такое же, как .py (но с расширением .md)
    md_filename = py_file.stem + ".md"
    md_path = output_dir / md_filename

    # Создаём красивый заголовок
    title = make_title(py_file.name)

    # Содержимое Markdown файла
    content = f"""# {title}

--8<-- "{relative_path}"
"""

    # Записываем файл
    md_path.write_text(content, encoding='utf-8')
    print(f"✓ Создан: {md_path}")


# Создаём директории для документации
def setup_dirs():
    """Создаёт необходимые директории"""
    DOCS_DIR.mkdir(exist_ok=True)
    DOCS_NOTES_DIR.mkdir(exist_ok=True)
    DOCS_LEETCODE_DIR.mkdir(exist_ok=True)


# Генерация index.md для раздела
def create_index(output_dir, title, description, files):
    """
    Создаёт index.md с содержанием раздела

    Args:
        output_dir: куда сохранить index.md
        title: заголовок раздела
        description: описание
        files: список файлов для включения в оглавление
    """
    index_path = output_dir / "index.md"

    content = f"""# {title}

{description}

## Содержание

"""

    # Добавляем ссылки на каждый файл
    for f in sorted(files):
        file_title = make_title(f.name)
        link = f"{f.stem}.md"
        content += f"- [{file_title}]({link})"

    index_path.write_text(content, encoding='utf-8')
    print(f"✓ Создан индекс: {index_path}")


# Основная функция генерации
def generate_docs():
    """Главная функция - генерирует всю документацию"""

    print("🚀 Начинаем генерацию документации...")

    # Создаём структуру папок
    setup_dirs()

    # === Обработка notes/ ===
    if NOTES_DIR.exists():
        print("📝 Обработка Python заметок...")
        py_files = list(NOTES_DIR.glob("*.py"))

        if py_files:
            for py_file in py_files:
                # Пропускаем __pycache__ и файлы с "__"
                if py_file.name.startswith("_"):
                    continue

                relative_path = f"notes/{py_file.name}"
                create_md_for_py(py_file, DOCS_NOTES_DIR, relative_path)

            # Создаём index.md для notes
            valid_files = [f for f in py_files if not f.name.startswith("_")]
            create_index(
                DOCS_NOTES_DIR,
                "Python заметки",
                "Здесь собраны мои заметки по различным концепциям Python с примерами кода.",
                valid_files
            )
        print()

    # === Обработка solutions/ (LeetCode) ===
    if SOLUTIONS_DIR.exists():
        print("🎯 Обработка решений LeetCode...")
        solution_files = list(SOLUTIONS_DIR.glob("*.py"))

        if solution_files:
            for py_file in solution_files:
                if py_file.name.startswith("_"):
                    continue

                relative_path = f"solutions/{py_file.name}"
                create_md_for_py(py_file, DOCS_LEETCODE_DIR, relative_path)

            # Создаём index.md для leetcode
            valid_files = [f for f in solution_files if not f.name.startswith("_")]
            create_index(
                DOCS_LEETCODE_DIR,
                "LeetCode решения",
                "Коллекция моих решений задач с LeetCode.",
                valid_files
            )
        print()

    # === Создаём главную страницу ===
    print("📄 Создание главной страницы...")
    main_index = DOCS_DIR / "index.md"

    notes_count = len(list(NOTES_DIR.glob("*.py"))) if NOTES_DIR.exists() else 0
    solutions_count = len(list(SOLUTIONS_DIR.glob("*.py"))) if SOLUTIONS_DIR.exists() else 0

    main_content = f"""# LEETCODEANDPYTHON

Добро пожаловать в мою базу знаний по Python!

## О проекте

Этот проект содержит:

- **{notes_count} Python заметок** — объяснения концепций с примерами кода
- **{solutions_count} LeetCode решений** — разборы алгоритмических задач

## Навигация

### [Python заметки](notes/index.md)
Заметки по основам и продвинутым концепциям Python: decorators, generators, context managers и многое другое.

### [LeetCode](leetcode/index.md)
Решения задач с LeetCode с подробными комментариями и объяснениями.

## Как использовать

Все примеры кода можно копировать и запускать локально. Используйте поиск (🔍) для быстрого нахождения нужной темы.

---

*Документация автоматически сгенерирована из исходников Python*
"""

    main_index.write_text(main_content, encoding='utf-8')
    print(f"✓ Создан: {main_index}")

    print("✅ Генерация завершена успешно!")
    print(f"\n📊 Статистика:")
    print(f"   • Python заметок: {notes_count}")
    print(f"   • LeetCode решений: {solutions_count}")
    print(f"\n💡 Следующие шаги:")
    print(f"   1. Запустите: mkdocs serve")
    print(f"   2. Откройте: http://127.0.0.1:8000")


if __name__ == "__main__":
    generate_docs()
