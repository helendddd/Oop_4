#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.ex2 import generate_matrix


def test_matrix_2x3() -> None:
    matrix_2x3 = generate_matrix(2, 3, 1, 5)
    assert len(matrix_2x3) == 2  # Проверка числа строк
    assert all(len(row) == 3 for row in matrix_2x3)  # Проверка числа столбцов
    assert all(1 <= num <= 5 for row in matrix_2x3 for num in row)


def test_matrix_negative_values() -> None:
    matrix_negative = generate_matrix(2, 2, -10, -1)
    assert len(matrix_negative) == 2
    assert all(len(row) == 2 for row in matrix_negative)
    assert all(-10 <= num <= -1 for row in matrix_negative for num in row)


def test_zero_rows_cols() -> None:
    try:
        generate_matrix(0, 3, 1, 10)
    except ValueError as e:
        assert str(e) == "Число строк и столбцов должно быть больше нуля."


def test_min_greater_than_max() -> None:
    try:
        generate_matrix(3, 3, 10, 1)
    except ValueError as e:
        assert str(e) == "Минимальное значение не может быть больше максимума"


def test_matrix_4x4_full_range() -> None:
    matrix_4x4 = generate_matrix(4, 4, 1, 100)
    assert len(matrix_4x4) == 4
    assert all(len(row) == 4 for row in matrix_4x4)
    assert all(1 <= num <= 100 for row in matrix_4x4 for num in row)
