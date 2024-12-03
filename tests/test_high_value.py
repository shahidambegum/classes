from lib.high_value import HighValue
def test_get_highest_returns_first_value_is_higher():
    values = HighValue(3, 1)
    result = values.get_highest()
    assert result == "First value is higher"

def test_get_highest_returns_second_value_is_higher():
    values = HighValue(1, 3)
    result = values.get_highest()
    assert result == "Second value is higher"

def test_get_highest_returns_values_are_equal():
    values = HighValue(3, 3)
    result = values.get_highest()
    assert result == "Values are equal"

def test_add_returns_increased_first_value_by_1():
    values = HighValue(3, 1)
    values.add(1, "first")
    assert values.value_first == 4
    assert values.value_second == 1

def test_add_returns_increased_second_value_by_1():
    values = HighValue(3, 1)
    values.add(1, "second")
    assert values.value_first == 3
    assert values.value_second == 2