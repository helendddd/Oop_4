#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main() -> None:
    """
    Запрашивает ввод двух значений. Если оба являются числами, суммирует их.
    Если хотя бы одно не число, выполняет конкатенацию строк.
    """
    # Запрашиваем первое значение
    first_value = input("Первое значение: ")

    # Запрашиваем второе значение
    second_value = input("Второе значение: ")

    # Проверяем, являются ли оба значения числами
    try:
        # Пытаемся преобразовать оба значения в числа (float)
        num1 = float(first_value)
        num2 = float(second_value)
        # Если оба значения числа, выполняем их суммирование
        result: float = num1 + num2
        print("Результат:", result)
    except ValueError:
        # Если хотя бы одно из значений не число, выполняем конкатенацию
        result: str = first_value + second_value
        print("Результат:", result)


if __name__ == "__main__":
    main()
