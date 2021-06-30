import unittest


class TestSum(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(sum([1, 2, 3]), 5, "Should be 6")

    def test_assert_not_equal(self):
        self.assertNotEqual(sum([1, 2, 3]), 6, "Should not be 6")

    def test_assert_true(self):
        testValue = False
        message = "Test value is not true"
        self.assertTrue(testValue, message)

    def test_assert_false(self):
        testValue = True
        message = "Test value is not true"
        self.assertFalse(testValue, message)

    def test_assert_is(self):
        firstValue = 1
        secondValue = 2
        message = "Test values are not equal"
        self.assertIs(firstValue, secondValue, message)

    def test_assert_is_not(self):
        firstValue = 1
        secondValue = 1
        message = "Test values are equal"
        self.assertIsNot(firstValue, secondValue, message)

    def test_assert_is_none(self):
        testValue = "test"
        message = "Test value is not none"
        self.assertIsNone(testValue, message)

    def test_assert_is_not_none(self):
        testValue = None
        message = "Test value is none"
        self.assertIsNotNone(testValue, message)

    def test_assert_in(self):
        my_list = [1, 5, 10, 30]
        self.assertIn(50, my_list, "not in list")

    def test_assert_not_in(self):
        my_list = [1, 5, 10, 30]
        self.assertNotIn(10, my_list, "not in list")

    def test_assert_is_instance(self):
        class Mytest:
            x = 2
        class Mytest2:
            x = 3
        objectName = Mytest()
        message = "given object is not instance of Myclass."
        self.assertIsInstance(objectName, Mytest2, message)

    def test_assert_not_is_instance(self):
        class Mytest:
            x = 2
        class Mytest2:
            x = 3
        objectName = Mytest()
        message = "given object is instance of Myclass."
        self.assertNotIsInstance(objectName, Mytest, message)

    def test_assert_almost_equal(self):
        first = 0.1488
        second = 0.1499
        decimalPlace = 3
        message = "first and second are not almost equal"
        self.assertAlmostEqual(first, second, decimalPlace, message)

    def test_assert_not_almost_equal(self):
        first = 0.1488
        second = 0.1499
        decimalPlace = 2
        message = "first and second are almost equal"
        self.assertNotAlmostEqual(first, second, decimalPlace, message)

    def test_assert_greater(self):
        self.assertGreater(5, 6, "Value is not greater")

    def test_assert_greater_equal(self):
        self.assertGreaterEqual(5, 6, "Value is not greater or equal")

    def test_assert_less(self):
        self.assertLess(7, 6, "Value is not less")

    def test_assert_less_equal(self):
        self.assertLessEqual(10, 6, "Value is not less or equal")


if __name__ == '__main__':
    unittest.main()
