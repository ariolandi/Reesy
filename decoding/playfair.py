from dependencies.decorators import verify_types
from dependencies.text_transformation_utils import to_pairs
from string import ascii_uppercase as LETTERS


@verify_types([])
def get_possible_rows(pairs):
    def get_letter_matches(letter, pairs):
        return [y if x == letter else x for x, y in set(pairs)
                if letter in [x, y]]

    matches = {letter: get_letter_matches(letter, pairs) for letter in LETTERS}

    possible_rows = []
    for x in LETTERS:
        for i, y in enumerate(matches[x]):
            possible_rows.append(set([x, y] + [z for z in matches[x][i:]
                                               if z in matches[y]]))

    return possible_rows


@verify_types(str)
def playfair(text):
    if len(text) % 2:
        text.append('A')

    pairs = to_pairs(text)
    possible_rows = get_possible_rows(pairs)
