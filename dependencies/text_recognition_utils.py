from dependencies.common import filter_list
from dependencies.constants import FOLLOWING_RILES
from dependencies.text_transformation_utils import only_letters, to_bigrams
from dependencies.decorators import verify_types
from string import ascii_letters as LETTERS

LANGUAGE = 'en'
DESIRED_LANGUAGE_PROBABILITY = 0.99999


@verify_types(str)
def text_statistics(text):
    """
    Generates the frequence table for a given text.
    """

    all_letters = len(filter_list((lambda x: x.isalpha()), text))

    return {letter: text.count(letter) / all_letters for letter in LETTERS}


@verify_types(str)
def analyze_for_consistency(text):
    """
    Analizes a given text for known rules about the bigrapghs in it.
    """

    bigrams = to_bigrams(only_letters(text))
    return all([FOLLOWING_RILES[x] == y for x, y in bigrams
                if x in FOLLOWING_RILES.keys()])


@verify_types(str)
def is_english_text(text):
    """"
    Detects the most probable language for a given text.
    Returns True if that language is English.
    """

    from langdetect import detect_langs

    possible_languages = {language.lang: language.prob
                          for language in detect_langs(text)}
    return LANGUAGE in possible_languages.keys() and\
        possible_languages[LANGUAGE] > DESIRED_LANGUAGE_PROBABILITY


@verify_types(str)
def is_valid_text(text):
    return analyze_for_consistency(text) and is_english_text(text)
