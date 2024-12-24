#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from unittest.mock import patch

from src.ex1 import main


def test_sum_of_numbers() -> None:
    with patch("builtins.input", side_effect=["5", "7"]), patch(
        "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        main()
        output = mock_stdout.getvalue().strip()
        assert "Результат: 12.0" in output


def test_concatenation_of_strings() -> None:
    with patch("builtins.input", side_effect=["hello", "world"]), patch(
        "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        main()
        output = mock_stdout.getvalue().strip()
        assert "Результат: helloworld" in output


def test_number_and_string() -> None:
    with patch("builtins.input", side_effect=["5", "hello"]), patch(
        "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        main()
        output = mock_stdout.getvalue().strip()
        assert "Результат: 5hello" in output


def test_invalid_inputs() -> None:
    with patch("builtins.input", side_effect=["abc", "123"]), patch(
        "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        main()
        output = mock_stdout.getvalue().strip()
        assert "Результат: abc123" in output


def test_negative_numbers() -> None:
    with patch("builtins.input", side_effect=["-5", "-3"]), patch(
        "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        main()
        output = mock_stdout.getvalue().strip()
        assert "Результат: -8.0" in output
