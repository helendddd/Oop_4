#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


def generate_matrix(rows, cols, min_val, max_val):
    """Генерирует матрицу случайных целых чисел."""
    if rows <= 0 or cols <= 0:
        raise ValueError("Число строк и столбцов должно быть больше нуля.")
    if min_val > max_val:
        raise ValueError("Минимальное значение не может быть больше максимума")

    return [
        [random.randint(min_val, max_val) for _ in range(cols)]
        for _ in range(rows)
    ]


def main():
    print("Программа для генерации матрицы из случайных целых чисел.")
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))
        min_val = int(input("Введите минимальное значение: "))
        max_val = int(input("Введите максимальное значение: "))

        matrix = generate_matrix(rows, cols, min_val, max_val)
        print("Сгенерированная матрица:")
        for row in matrix:
            print(row)

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
