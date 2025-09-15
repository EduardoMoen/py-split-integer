from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    expected = [5, 5, 5]
    actual = split_integer(15, 3)
    assert actual == expected


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    expected = [4, 4, 4, 4]
    actual = split_integer(16, 4)
    assert actual == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    expected = [5]
    actual = split_integer(5, 1)
    assert actual == expected


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    expected = [5, 5, 5, 5, 6, 6]
    actual = split_integer(32, 6)
    assert actual == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    expected = [0, 1, 1, 1, 1]
    actual = split_integer(4, 5)
    assert actual == expected
