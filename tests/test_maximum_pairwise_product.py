import unittest
from parameterized import parameterized_class
from algos.algorithmic_toolbox.week_one.maximum_pairwise_product import max_pairwise_product_brute_force, \
    max_pairwise_product_sort, max_pairwise_product_linear


@parameterized_class(('array', 'answer'), [
    ([1, 5, 3, 6, 8, 11, 10, 1, 0], 110),
    ([], 0),
    ([0, 0, 0, 1], 0),
    ([1, 1, 1, 1], 1),
    ([10, 9, 3, 1, 0], 90),
    ([3, 3, 3, 3], 9),
])
class TestSumOfTwoDigits(unittest.TestCase):

    def test_max_pairwise_product_brute_force(self):
        self.assertEqual(max_pairwise_product_brute_force(self.array), self.answer)


    def test_max_pairwise_product_sort(self):
        self.assertEqual(max_pairwise_product_sort(self.array), self.answer)


    def test_max_pairwise_product_linear(self):
        self.assertEqual(max_pairwise_product_linear(self.array), self.answer)


if __name__ == '__main__':
    unittest.main()
