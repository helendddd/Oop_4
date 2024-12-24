import io
import json
import sys

from src.gradebook import add_student, find, list_students, load_students, save


def test_add_student():
    """Тест добавления нового студента."""
    students = []
    name = "Иванов И.И."
    group_number = "1234"
    performance = [5, 4, 3, 4, 5]

    updated_students = add_student(students, name, group_number, performance)

    assert len(updated_students) == 1, "Ошибка: Студент не был добавлен"
    assert updated_students[0]["name"] == name, "Ошибка: Неверное имя студента"
    assert (
        updated_students[0]["group_number"] == group_number
    ), "Ошибка: Неверный номер группы"
    assert (
        updated_students[0]["performance"] == performance
    ), "Ошибка: Неверные оценки"


def test_list_students():
    """Тест вывода списка студентов."""
    students = [
        {
            "name": "Иванов И.И.",
            "group_number": "1234",
            "performance": [5, 4, 3, 4, 5],
        },
        {
            "name": "Петров П.П.",
            "group_number": "5678",
            "performance": [3, 4, 5, 5, 4],
        },
    ]

    # Мокируем функцию print с помощью io.StringIO
    captured_output = io.StringIO()
    sys.stdout = captured_output  # Перенаправляем stdout в StringIO

    list_students(students)

    # Проверим, что функция вывела строку с именами студентов
    output = captured_output.getvalue()
    print(output)  # Выведем для отладки

    # Проверка только наличия заголовка
    assert (
        "Фамилия и инициалы" in output
    ), "Ошибка: Неверный вывод списка студентов"
    assert (
        "Иванов И.И." in output
    ), "Ошибка: Студент Иванов И.И. не найден в выводе"


def test_find_students_with_2():
    """Тест поиска студентов с оценкой 2."""
    students = [
        {
            "name": "Иванов И.И.",
            "group_number": "1234",
            "performance": [5, 4, 3, 4, 5],
        },
        {
            "name": "Петров П.П.",
            "group_number": "5678",
            "performance": [2, 4, 5, 5, 4],
        },
    ]

    found_students = find(students)
    assert len(found_students) == 1, "Ошибка: Студент с оценкой 2 не найден"
    assert (
        found_students[0]["name"] == "Петров П.П."
    ), "Ошибка: Неверно найден студент"


def test_save_and_load_students():
    """Тест сохранения и загрузки данных студентов в/из файла."""
    students = [
        {
            "name": "Иванов И.И.",
            "group_number": "1234",
            "performance": [5, 4, 3, 4, 5],
        },
        {
            "name": "Петров П.П.",
            "group_number": "5678",
            "performance": [3, 4, 5, 5, 4],
        },
    ]

    save("test_students.json", students)

    # Проверим, что файл существует и можно загрузить данные
    loaded_students = load_students("test_students.json")
    assert len(loaded_students) == 2, "Ошибка: Неверное число студентов"
    assert (
        loaded_students[0]["name"] == "Иванов И.И."
    ), "Ошибка: Неверный студент при загрузке"
    assert (
        loaded_students[1]["name"] == "Петров П.П."
    ), "Ошибка: Неверный студент при загрузке"


def test_load_empty_file():
    """Тест загрузки пустого файла."""
    with open("test_students.json", "w") as f:
        f.write("[]")  # Пишем пустой список в файл

    students = load_students("test_students.json")
    assert students == [], "Ошибка: Не удалось загрузить пустой список"


def test_invalid_json_file():
    """Тест на случай, если файл имеет некорректный JSON."""
    with open("test_students.json", "w") as f:
        f.write("{ invalid json ")

    try:
        load_students("test_students.json")
        assert False, "Ожидалась ошибка при загрузке некорректного JSON"
    except json.JSONDecodeError:
        pass  # Ожидали исключение json.JSONDecodeError


if __name__ == "__main__":
    test_add_student()
    test_list_students()
    test_find_students_with_2()
    test_save_and_load_students()
    test_load_empty_file()
    test_invalid_json_file()

    print("Все тесты прошли успешно!")
