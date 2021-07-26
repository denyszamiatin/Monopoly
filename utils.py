import settings
import random


def throw_dice():
    """
    Throw the dice.
    :return: List of integers from settings.DICE_MIN
     to settings.DICE_MAX as a result of dice roll.
    """
    return tuple([random.randint(settings.DICE_MIN, settings.DICE_MAX)
                  for _ in range(settings.DICE_AMOUNT)])
