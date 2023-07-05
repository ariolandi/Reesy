from dependencies.text_transformation_utils\
    import shift_letter, find_possible_shift
from dependencies.text_recognition_utils import (text_statistics,
                                                 filter_only_valid)
from string import ascii_uppercase as LETTERS
from dependencies.common import count_values, flatten, filter_dict
from dependencies.decorators import verify_only_symbol, verify_types, upper


@upper
@verify_types(str)
def filter_keys(text):
    """
    Decides which keys are most likely used for the cipher.
    Uses the frequence table to decide if a given key is possible or not
    and returns only these key with above average probability.
    """

    frequency_table = text_statistics(text)
    keys_possibility = count_values(flatten(
                        [find_possible_shift(letter, frequency_table[letter])
                         for letter in LETTERS]))

    avrg_value = sum(keys_possibility.values()) / len(keys_possibility)
    return filter_dict((lambda y: y >= avrg_value), keys_possibility).keys()


@verify_types(str, int)
@verify_only_symbol
def transform(symbol, key):
    """
    Transforms a symbol with a given key (offset) if it is a letter.
    If the passed symbol is not a letter (punctuation, spacetab or number)
    it returns the symbol itself without transforming it.
    """

    return shift_letter(symbol, key) if symbol.isalpha() else symbol


@verify_types(str, int)
def caesar_with_key(text, key):
    return ''.join([transform(x, key) for x in text])


@verify_types(str)
def caesar(text):
    possible_keys = filter_keys(text)
    all_texts = [caesar_with_key(text, key) for key in possible_keys]
    return filter_only_valid(all_texts)
