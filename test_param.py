import pytest


# class TestParam:
#     def is_greater_than(self, n, m):
#         return n > m
#
#     @pytest.mark.parametrize(("a", "b"), [(0, 5), (6, 100500)])
#     def test_example(self, a, b):
#         print("\nthis is positive test")
#         assert self.is_greater_than(a, b)

example = [0, 5, 3, 1, 6, 6]
booleans = [False, False, True, False]

def test_example():
    print(all(example)) # Success Example
    print(any(booleans)) # Success Example


