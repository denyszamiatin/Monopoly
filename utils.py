import settings
import random


def throw_dice():
    """
    Throw the dice.
    :return: List of integers from settings.DICE_MIN to settings.DICE_MAX as a result of dice roll.
    """
    return [random.randint(settings.DICE_MIN, settings.DICE_MAX) for _ in range(settings.DICE_AMOUNT)]


def validate_dice_throw() ->list[int]:
    """
    Randomize dice throw.
    :return: Values from 1 to 6, as a list of integers.
    """
    count = 0
    while True:
        if count < 3:
            rand_list = throw_dice()
            if len(rand_list) == len(set(rand_list)):
                return rand_list
            else:
                count += 1
                return rand_list
        else:
            """ TODO: create field jail and using function move, put player into jail."""
            pass