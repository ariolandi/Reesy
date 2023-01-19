ALPHABET_START = ord('A')
ALPHABET_SIZE = 26

# Please note that all letters are expected to be uppercese
# Source: http://practicalcryptography.com/

LETTER_STATISTIC = {
    'E': 11.1607, 'A': 8.4966, 'R': 7.5809,
    'I':  7.5448, 'O': 7.1635, 'T': 6.9509,
    'N':  6.6544, 'S': 5.7351, 'L': 5.4893,
    'C':  4.5388, 'U': 3.6308, 'D': 3.3844,
    'P':  3.1671, 'M': 3.0129, 'H': 3.0034,
    'G':  2.4700, 'B': 2.0720, 'F': 1.8121,
    'Y':  1.7779, 'W': 1.2899, 'K': 1.1016,
    'V':  1.0074, 'X': 0.2902, 'Z': 0.2722,
    'J':  0.1965, 'Q': 0.1962
}

BIGRAMS_STATISTICS = {
    'TH': 2.71, 'HE': 2.33, 'IN': 2.03,
    'ER': 1.78, 'AN': 1.61, 'RE': 1.41,
    'ES': 1.32, 'ON': 1.32, 'ST': 1.25,
    'NT': 1.17, 'EN': 1.13, 'AT': 1.12,
    'ED': 1.08, 'ND': 1.07, 'TO': 1.07,
    'OR': 1.06, 'EA': 1.00, 'TI': 0.99,
    'AR': 0.98, 'TE': 0.98, 'NG': 0.89,
    'AL': 0.88, 'IT': 0.88, 'AS': 0.87,
    'IS': 0.86, 'HA': 0.83, 'ET': 0.76,
    'SE': 0.73, 'OU': 0.72, 'OF': 0.71
}

COMMON_WORDS = {
    'THE':  6.42, ' OF': 2.76,  'AND': 2.75,
    'TO':   2.67,   'A': 2.43,   'IN': 2.31,
    'IS':   1.12, 'FOR': 1.01, 'THAT': 0.92,
    'WAS':  0.88,  'ON': 0.78, 'WITH': 0.75,
    'HE':   0.75,  'IT': 0.74,   'AS': 0.71,
    'AT':   0.58, 'HIS': 0.55,   'BY': 0.51,
    'FROM': 0.47, 'ARE': 0.47, 'THIS': 0.42,
    'I':    0.41, 'BUT': 0.40, 'HAVE': 0.39,
    'AN':   0.37, 'HAS': 0.35,  'NOT': 0.34,
    'THEY': 0.33,  'OR': 0.30,   'BE': 0.48
}

FREQUENTLY_DOUBLED_LETTERS = ['SS', 'LL', 'OO',  'EE', 'NN', 'PP']

# Q is unuque for English language - it is always followed by letter U
FOLLOWING_RILES = {'Q': 'U'}

SUBSTITUTION_RULES = {'_': ' '}

MAX_DIFFERENCE = 1.0
