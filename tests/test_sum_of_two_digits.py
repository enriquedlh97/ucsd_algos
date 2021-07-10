import unittest
from parameterized import parameterized_class
from algos.algorithmic_toolbox.week_one.sum_of_two_digits import sum_of_two_products


@parameterized_class(('first_digit', 'second_digit', 'answer'), [
    (1, 2, 1 + 2),
    (3, 4, 3 + 4),
    (-1, 1, -1 + 1),
    (100, 2, 100 + 2),
    (123, 456, 123 + 456),
])
class TestSumOfTwoDigits(unittest.TestCase):

    def test_sum_of_two_products(self):
        self.assertEqual(sum_of_two_products(self.first_digit, self.second_digit), self.answer)
        

if __name__ == '__main__':
    unittest.main()
