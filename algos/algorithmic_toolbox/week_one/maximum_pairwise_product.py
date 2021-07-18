"""
Problem:

    Find the maximum product of two distinct numbers in a sequence of non-negative integers.

Input:

    A sequence of non-negative integers

    sample_input: [1, 2, 3, 7, 4, 6]

Output:

    The maximum value that can be obtained by multiplying two different elements from the sequence.

    sample_output: 42 # Given by 7 * 6
"""


# Time: O(n^2) where n is the length of the input array
# Space: O(1)
def max_pairwise_product_brute_force(array):
    """ Brute fore solution

    This solution works by iterating once over the array and then, for each value, another iteration over the input
    array is performed. For each step the product of the two values is computed. The maximum product is being kept track
    of and at the end is returned as final value.

    :param array: array of non-negative integers
    :return: integer value corresponding to the maximum product of two distinct numbers from the input array
    """

    if len(array) <= 1:
        return 0

    max_product = 0

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                if array[i] * array[j] > max_product:
                    max_product = array[i] * array[j]

    return max_product


# Time: O(n * lg(n)) where n is the length of the input array
# Space: O(1)
def max_pairwise_product_sort(array):
    """ Sorted array solution

    This solution works by sorting the input array in ascending order. Then the product of the two final values is
    returned as the final solution (2 biggest values).

    :param array: array of non-negative integers
    :return: integer value corresponding to the maximum product of two distinct numbers from the input array
    """
    if len(array) <= 1:
        return 0

    array.sort()

    return array[-1] * array[-2]


# Time: O(n) where n is the length of the input array
# Space: O(1)
def max_pairwise_product_linear(array):
    """ Linear time solution

    This solution iterates only once over yhe input array. At each step, the two biggest values are being saved.
    At the end, the product of these two biggest values is returned as the final solution.

    :param array: array of non-negative integers
    :return: integer value corresponding to the maximum product of two distinct numbers from the input array
    """

    if len(array) <= 1:
        return 0

    two_biggest_values = [0, 0]

    for element in array:
        if element > two_biggest_values[0]:
            two_biggest_values[0] = element
        elif element > two_biggest_values[1]:
            two_biggest_values[1] = element

    return two_biggest_values[0] * two_biggest_values[1]
