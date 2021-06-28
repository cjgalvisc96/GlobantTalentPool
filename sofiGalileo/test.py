"""
Given an array, return a new array exchanging the ﬁrst and last elements.
Example:
For arr = [1, 2, 3, 4], the output should be
exchange(arr) = [4, 2, 3, 1]
For arr = [1], the output should be
exchange(arr) = [1]
For arr = [], the output should be
exchange(arr) = []
"""


def exchanging_elements_in_array(
    *,
    array: list
) -> list:
    if array:
        array[0], array[-1] = array[-1], array[0]
    return array



"""
Given some integer, ﬁnd the maximal number you can obtain by deleting exactly 
one digit of the given number.
Example
For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
"""


def delete_digit(
    *,
    number: int
) -> int:
    min_digit = min(number)


if __name__ == '__main__':
    array_tests = [
        [1, 2, 3, 4],
        [1],
        []
    ]
    for array_test in array_tests:
        print(exchanging_elements_in_array(array=array_test))

    number_tests = [
        152, 1001
    ]
    for number_test in number_tests:
        print(delete_digit(number=number_test))
