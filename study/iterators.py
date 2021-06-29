"""
used for better the performance memory
"""


if __name__ == '__main__':
    # big_list = [x for x in range(1000000000000000000000)]
    big_list = iter(range(1000000000000000000000))
    print(next(big_list))
