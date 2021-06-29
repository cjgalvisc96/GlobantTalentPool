def my_customize_decorator(function):
    def wrapper(*args, **kwargs):
        print("Before function")
        function(*args, **kwargs)
        print("After function")

    return wrapper


@my_customize_decorator
def _sum(*, num_1, num_2):
    print(num_1 + num_2)


if __name__ == '__main__':
    _sum(num_1=2, num_2=3)
