import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test_assert_equal(self):
        self.assertGreater(5, 6, "5 is not greater")

    def test_assert_in(self):
        my_list = [1, 5, 10, 30]
        self.assertIn(50, my_list, "not in list")

    def test_assert_not_in(self):
        my_list = [1, 5, 10, 30]
        self.assertNotIn(10, my_list, "not in list")

if __name__ == '__main__':
    unittest.main()