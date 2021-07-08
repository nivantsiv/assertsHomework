import pytest
from collections.abc import Iterable

class TestExample:
    @pytest.mark.usefixtures("after_first_test")
    def test_example(self):
        print("\nthis is test")
        assert 1 == 1

    def test_1example(self):
        print("\nthis is test2")
        assert 2 > 1

    def test_2example(self):
        print("\nthis is test3")
        assert 3 != 1

    def test_3example(self):
        print("\nthis is test4")
        assert 3 < 5

    def test_assert_equal(self):
        assert sum([1, 2, 2]) == 6, "Should be 6"

    def test_assert_type(self):
        assert type(5) is float

    def test_assert_instance(self):
        x = "5.2"
        assert isinstance(x, int), type(x)

    def test_assert_is_instance(self):
        assert isinstance('5', str)

    def test_assert_in(self):
        my_list = [1, 5, 10, 30]
        assert 50 in my_list, "not in list"

    def test_assert_in_true(self):
        my_list = [1, 5, 10, 30]
        assert 5 in my_list, "not in list"

    def test_assert_boolean(self):
        true = 5 == 5
        assert true is True

    def test_assert_boolean_false(self):
        true = 5 == 5
        assert true is False

    def test_assert_modulus(self):
        assert 500 % 3 == 2

    def test_assert_any(self):
        example = [0, 5, 3, 1, 6, 6]
        assert any(example) == True

    def test_assert_any_bool(self):
        booleans = [False, False, True, False]
        assert any(booleans) == True

    def test_assert_all(self):
        example = [0, 5, 3, 1, 6, 6]
        assert all(example) == True

    def test_assert_all_bool(self):
        booleans = [False, False, True, False]
        assert all(booleans) == True

    def test_assert_iterable(self):
        iterable_item = [3, 6, 4, 2, 1]
        assert isinstance(5, Iterable)

    def test_assert_string(self):
        my_variable = "s"
        assert isinstance(my_variable, str)


@pytest.fixture(autouse=True)
def after_each_test():
    yield
    print("\nafter each test")

@pytest.fixture(autouse=True)
def before_each_test():
    print("\nbefore each test")
    yield

@pytest.fixture()
def after_first_test():
    yield
    print("\nthis is specific test")
