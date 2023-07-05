from dependencies.decorators import verify_types
from dependencies.common import equalize_frequences, count_values
from dependencies.text_transformation_utils import (to_pairs,
                                                    find_possible_match)
from dependencies.text_recognition_utils import text_statistics, histogram
from dependencies.constants import (MAX_DIFFERENCE_REDUCED,
                                    BIGRAMS_STATISTICS, MAX_BIGRAMS_DIFFERENCE)
from string import ascii_uppercase as LETTERS
from pprint import pprint


def get_possible_rows(pair_possibility, letter_possibility):
    def _possible_match(pair_a, pair_b):
        def _possible_decoding(a, b):
            return a in letter_possibility[b]

        return (_possible_decoding(pair_a[0], pair_b[0]) or
                _possible_decoding(pair_a[1], pair_b[1])) and\
            pair_a[0] != pair_b[0] and pair_a[1] != pair_b[1]

    pair_possibility = [(key, value) for key, value in pair_possibility.items()]
    pair_possibility.sort(key=lambda x: len(x[1]))

    possible_decodings = {pair: [(x[0], x[1]) for x in possibility
                                 if _possible_match(x, pair)]
                          for pair, possibility in pair_possibility}

    pprint(possible_decodings)

@verify_types(str)
def playfair(text):
    if len(text) % 2:
        text.append('_')

    frequency_table = text_statistics(text)
    letter_possibility = {letter: find_possible_match(frequency_table[letter],
                                                      MAX_DIFFERENCE_REDUCED)
                          for letter in LETTERS}

    pairs = to_pairs(text)
    pairs_frequency = equalize_frequences(histogram(pairs), BIGRAMS_STATISTICS)

    pairs_possibility = {pair: find_possible_match(pairs_frequency[pair],
                                                   MAX_BIGRAMS_DIFFERENCE,
                                                   BIGRAMS_STATISTICS)
                         for pair in pairs}

    # pprint(pairs_frequency)
    get_possible_rows(pairs_possibility, letter_possibility)
