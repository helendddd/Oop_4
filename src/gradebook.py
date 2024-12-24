#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import os.path
import pathlib

import jsonschema

# Конфигурация логгера
logging.basicConfig(
    filename="students_program.log",
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def add_student(students, name, group_number, performance):
    """Функция для добавления нового ученика в список."""
    try:
        students.append(
            {
                "name": name,
                "group_number": group_number,
                "performance": performance,
            }
        )
        logging.info(f"Добавлен новый студент: {name}, Группа: {group_number}")
    except Exception as e:
        logging.error(f"Ошибка при добавлении студента: {e}")
        raise
    return students


def list_students(students):
    """Функция для вывода списка студентов."""
    try:
        if students:
            line = "+-{}-+-{}-+-{}-+-{}-+".format(
                "-" * 4, "-" * 30, "-" * 20, "-" * 20
            )
            print(line)

            print(
                "| {:^4} | {:^30} | {:^20} | {:^20} |".format(
                    "No", "Фамилия и инициалы", "Номер группы", "Успеваемость"
                )
            )

            print(line)

            for idx, student in enumerate(students, 1):
                print(
                    "| {:>4} | {:<30} | {:<20} | {:>20} |".format(
                        idx,
                        student.get("name", ""),
                        student.get("group_number", ""),
                        ", ".join(map(str, student.get("performance", []))),
                    )
                )
            print(line)
        else:
            print("Список студентов пуст.")
    except Exception as e:
        logging.error(f"Ошибка при выводе списка студентов: {e}")
        raise


def find(students):
    """Функция для поиска студентов с отметкой 2."""
    try:
        found = []

        for student in students:
            if 2 in student["performance"]:
                found.append(student)

        if not found:
            print("Студентов с отметкой 2 не найдено")
            logging.info("Не найдено студентов с оценкой 2.")
        else:
            list_students(found)
            logging.info(f"Найдено студентов с оценкой 2: {len(found)}")
        return found
    except Exception as e:
        logging.error(f"Ошибка при поиске студентов: {e}")
        raise


def save(file_name, students):
    """Сохранить всех студентов в файл JSON."""
    try:
        with open(file_name, "w", encoding="utf-8") as fout:
            json.dump(students, fout, ensure_ascii=False, indent=4)
            logging.info(f"Данные студентов сохранены в файл: {file_name}")
    except Exception as e:
        logging.error(f"Ошибка при сохранении данных в файл: {e}")
        raise


def load_students(file_name):
    """Загрузить всех студентов из файла JSON."""
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "group_number": {"type": "string"},
                "performance": {
                    "type": "array",
                    "items": {"type": "integer"},
                    "minItems": 5,
                    "maxItems": 5,
                },
            },
            "required": ["name", "group_number", "performance"],
        },
    }

    try:
        with open(file_name, "r", encoding="utf-8") as fin:
            loaded = json.load(fin)
        jsonschema.validate(loaded, schema)
        logging.info(f"Данные успешно загружены из файла: {file_name}")
        return loaded
    except jsonschema.exceptions.ValidationError as e:
        logging.error(
            f"Ошибка валидации данных в файле {file_name}: " f"{e.message}"
        )
        raise
    except Exception as e:
        logging.error(f"Ошибка при загрузке данных из файла: {e}")
        raise


def main():
    """Главная функция программы."""
    try:
        # Создать родительский парсер для определения имени файла.
        file_parser = argparse.ArgumentParser(add_help=False)
        file_parser.add_argument(
            "filename", action="store", help="The name of data file."
        )
        file_parser.add_argument(
            "--home",
            action="store_true",
            help="Save data file in home directory.",
        )

        # Создать основной парсер командной строки.
        parser = argparse.ArgumentParser("students")
        parser.add_argument(
            "--version", action="version", version="%(prog)s 0.1.0"
        )
        subparsers = parser.add_subparsers(dest="command")

        # Субпарсер для добавления студента.
        add = subparsers.add_parser(
            "add", parents=[file_parser], help="Add a new student"
        )
        add.add_argument(
            "-n",
            "--name",
            action="store",
            required=True,
            help="Student's name",
        )
        add.add_argument(
            "-g", "--group", action="store", help="Student's group number"
        )
        add.add_argument(
            "-p",
            "--performance",
            nargs=5,
            type=int,
            required=True,
            help="Student's performance (list of five marks)",
        )

        # Субпарсер для отображения всех студентов.
        subparsers.add_parser(
            "display", parents=[file_parser], help="Display all students"
        )

        # Субпарсер для нахождения студентов с оценкой "2".
        subparsers.add_parser(
            "find", parents=[file_parser], help="Find the students"
        )

        # Разбор аргументов командной строки.
        args = parser.parse_args()

        # Загрузка данных студентов из файла
        if args.home:
            filepath = pathlib.Path.home() / args.filename
        else:
            filepath = pathlib.Path(args.filename)

        if os.path.exists(filepath):
            students = load_students(filepath)
        else:
            students = []

        is_dirty = False  # Отслеживание изменений в списке студентов.

        # Обработка команд
        if args.command == "add":
            students = add_student(
                students, args.name, args.group, args.performance
            )
            is_dirty = True
        elif args.command == "display":
            list_students(students)
        elif args.command == "find":
            find(students)

        # Сохранение данных в файл, если они были изменены
        if is_dirty:
            save(filepath, students)

        logging.info(f"Команда '{args.command}' выполнена успешно.")

    except Exception as e:
        logging.error(f"Ошибка при выполнении команды: {e}")
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
