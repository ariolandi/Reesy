from dependencies.constants import (ALPHABET_SIZE, ALPHABET_START,
                                    LETTER_STATISTIC, DIFFERENCE,
                                    SUBSTITUTION_RULES)
from dependencies.decorators import verify_types, upper, verify_only_symbol


@verify_types(str)
def only_letters(text: str) -> list:
    return [x for x in text if x.isalpha()]


@verify_types((str, []))
def to_bigrams(text: list) -> list:
    return [(x, text[i + 1]) for i, x in enumerate(text[:-1])]


@verify_types((str, []))
def to_pairs(text: list) -> list:
    return [(text[i], text[i + 1]) for i in range(0, len(text), 2)]


@verify_types(str)
@upper
@verify_only_symbol
def order_in_alphabet(letter: str) -> int:
    return ord(letter) - ALPHABET_START


@verify_types(int)
def normalize(x: int) -> int:
    return x % ALPHABET_SIZE


@verify_types(int, int)
def shift(letter: int, positions: int) -> int:
    return normalize(letter + positions)


def shift_backwards(letter: int, positions: int) -> int:
    return shift(letter, positions * -1)


@verify_types(int)
def to_letter(order_of_letter: int) -> str:
    return chr(ALPHABET_START + order_of_letter)


@verify_types(str, int)
def shift_letter(letter: str, positions: int) -> str:
    return to_letter(shift(order_in_alphabet(letter), positions))


@verify_types(float, float)
def _is_possible_key(letter_frequency, key_fr, difference=DIFFERENCE):
    diff = abs(letter_frequency - key_fr)
    return difference['MIN'] <= diff and diff <= difference['MAX']


@verify_types(str, float)
@verify_only_symbol
def find_possible_match(letter: str, frequency: float) -> list:
    return [possible_match
            for possible_match, letter_fr in LETTER_STATISTIC.items()
            if _is_possible_key(frequency, letter_fr)]


@verify_types(str, float)
@verify_only_symbol
def find_possible_shift(letter: str, frequency: float) -> list:
    posible_decoding = [order_in_alphabet(possible_match)
                        for possible_match
                        in find_possible_match(letter, frequency)]

    return [shift_backwards(order_in_alphabet(letter), possible_match)
            for possible_match in posible_decoding]


@verify_types(str)
def substitute(text):
    def transform(text, rule, substitute):
        return substitute.join([word for word in text.split(rule) if word])

    for rule in SUBSTITUTION_RULES.keys():
        text = transform(text, rule, SUBSTITUTION_RULES[rule])

    return text
