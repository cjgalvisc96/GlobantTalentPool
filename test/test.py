def test_args_function(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    test_args_function(2, b=1, c=2)

