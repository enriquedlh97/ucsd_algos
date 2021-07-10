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
    array.sort()

    return array[-1] * array[-2]


# Time: O(n) where n is the length of the input array
# Space: O(1)
def max_pairwise_product_linear(array):
    two_biggest_values = [0, 0]

    for element in array:
        if element > two_biggest_values[0]:
            two_biggest_values[0] = element
        elif element > two_biggest_values[1]:
            two_biggest_values[1] = element

    return two_biggest_values[0] * two_biggest_values[1]
