"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREP_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes derived from `PREP_TIME_PER_LAYER`.

    Function that takes the number of layers in the lasagna as an argument and
    returns the preparation time in minutes.
    """

    return layers * PREP_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed baking time in minutes.
    :return: int - elapsed time in minutes derived from `number_of_layers` and
    `elapsed_bake_time`.

    Function that takes the number of layers in the lasagna and the elapsed baking
    time as arguments and returns the elapsed time in minutes.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
