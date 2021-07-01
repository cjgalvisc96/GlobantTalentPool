"""
Sintaxis:
    [expression FOR element IN iterable]

Teoria de conjuntos:
    - conjuntos por extensión - python -> (list)
        A = {1,2,3,4,5,6}
    - conjuntos por comprensión - python -> (comprehesion list)
        B = {X | X es un número entero entre el 1 y el 6}
"""


def range_in_six() -> tuple:
    extension_list = [1, 2, 3, 4, 5, 6]
    comprehension_list = [n for n in range(1, 7)]
    return extension_list, comprehension_list


def double_one_to_ten() -> list:
    comprehension_list = [n * 2 for n in range(11)]
    return comprehension_list


def asterisk_strings() -> list:
    comprehension_list = ["*" * n for n in range(1, 6)]
    return comprehension_list


def get_the_initials_of_the_words(
    *,
    words: list
) -> list:
    comprehension_list = [word[0] for word in words]
    return comprehension_list


def get_pairs_numbers(
    *,
    numbers: list
) -> list:
    comprehension_list = [number for number in numbers if number % 2 == 0]
    return comprehension_list


def get_words_with_seven_letters(
    *,
    words: list
) -> list:
    comprehension_list = [word for word in words if len(word) == 7]
    return comprehension_list


def using_else_sentence(
    *,
    numbers: list
) -> list:
    """
    include numbers pairs and numbers odd with "0"
    """
    comprehension_list = [
        number if number % 2 == 0 else 0 for number in numbers
    ]
    return comprehension_list


def get_elements_type_in_string_and_float(
    *,
    elements: list
) -> list:
    comprehension_list = [
        "string" if isinstance(element, str) else
        "integer" if isinstance(element, int) else
        None for element in elements
    ]
    return comprehension_list


if __name__ == '__main__':
    print(range_in_six())
    print(double_one_to_ten())
    print(asterisk_strings())
    print(get_the_initials_of_the_words(words=["Car", "Table", "Pc"]))
    print(get_pairs_numbers(numbers=[3, 6, 445, 12, 67, 8]))
    print(
        get_words_with_seven_letters(
            words=["Table", "academy", "sit", "account"]
        )
    )
    print(using_else_sentence(numbers=[3, 6, 445, 12, 67, 8]))
    print(
        get_elements_type_in_string_and_float(
            elements=[7, "h", 2.5, "m", 8.2, 24, "p"]
        )
    )
