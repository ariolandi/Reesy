from .constants import *
from .decorators import verify_types, upper, onlySymbol


@verify_types(str)
@upper
@onlySymbol
def order_in_alphabet(letter):
    return ord(letter) - ALPHABET_START


@verify_types(int)
def normalize(x):
    return x % ALPHABET_SIZE


@verify_types(int, int)
def shift_forward(letter, positions):
    return normalize(letter + positions)


@verify_types(int, int)
def shift_backward(letter, positions):
    return normalize(letter - positions)


@verify_types(int)
def to_letter(order_of_letter):
    return chr(ALPHABET_START + order_of_letter)


@verify_types(str, int)
def shift_letter_forward(letter, positions):
    return to_letter(shift_forward(order_in_alphabet(letter), positions))


@verify_types(str, int)
def shift_letter_backward(letter, positions):
    return to_letter(shift_backward(order_in_alphabet(letter), positions))


@verify_types(float, float, difference=float)
def _is_possible_key(letter_fr, key_fr, difference=MAX_DIFFERENCE):
    return abs(letter_fr - key_fr) <= difference


@verify_types(str, float)
@onlySymbol
def find_possible_shift(letter, frequency):
    posible_decoding = [order_in_alphabet(p_letter)
                        for p_letter, letter_fr in LETTER_STATISTIC.items()
                        if _is_possible_key(frequency, letter_fr)]
    return [shift_backward(order_in_alphabet(letter), p_letter)
            for p_letter in posible_decoding]
