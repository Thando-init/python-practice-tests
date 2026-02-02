import pytest
from assessment_five import *


# ========= BASIC TESTS =========

def test_count_occurrences():
    assert count_occurrences([1, 1, 2, 3, 3, 3]) == {1: 2, 2: 1, 3: 3}
    assert count_occurrences([]) == {}


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([]) == []


def test_format_price_list():
    result = format_price_list([10, 2.5, 3])
    assert "10.00" in result
    assert "2.50" in result


# ======= INTERMEDIATE TESTS =======

def test_split_by_type():
    items = [1, "a", 2, "b"]
    assert split_by_type(items) == {
        "integers": [1, 2],
        "strings": ["a", "b"]
    }


def test_recursive_max():
    assert recursive_max([1, 5, 3, 9, 2]) == 9


def test_transpose_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert transpose_matrix(matrix) == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


# ========= ADVANCED TESTS =========

def test_deep_count():
    assert deep_count([1, [2, [3, 4]], 5]) == 5


def test_recursive_string_reverse():
    assert recursive_string_reverse("abc") == "cba"
    assert recursive_string_reverse("") == ""


def test_generate_pascal_triangle():
    assert generate_pascal_triangle(1) == [[1]]
    assert generate_pascal_triangle(3) == [
        [1],
        [1, 1],
        [1, 2, 1]
    ]
