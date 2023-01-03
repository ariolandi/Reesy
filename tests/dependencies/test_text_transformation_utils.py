import unittest
from dependencies.text_transformation_utils import (
    only_letters, to_bigrams, normalize, shift,
    order_in_alphabet, shift_letter, shift_backwards,
    to_letter, find_possible_shift)


class TestOnlyLetters(unittest.TestCase):
    # only_letters(str) -> [str]

    def test_only_letter(self):
        self.assertEqual(only_letters(''), [])
        self.assertEqual(only_letters('123.,/  09'), [])
        self.assertEqual(only_letters('abcd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(only_letters('ab76 cd.j'), ['a', 'b', 'c', 'd', 'j'])

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            only_letters([])
        with self.assertRaises(TypeError):
            only_letters(857)


class TestToBigrams(unittest.TestCase):
    # to_bigrams([str]) -> [(str, str)]

    def test_to_bigrams(self):
        self.assertEqual(to_bigrams([]), [])
        self.assertEqual(to_bigrams(['a']), [])
        self.assertEqual(to_bigrams(['a', 'b', 'c', 'd']),
                         [('a', 'b'), ('b', 'c'), ('c', 'd')])

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            to_bigrams(8676)
        with self.assertRaises(TypeError):
            to_bigrams('adhgd')


class TestNormalize(unittest.TestCase):
    # normalize(int) -> int

    def test_normalize(self):
        self.assertEqual(normalize(2), 2)
        self.assertEqual(normalize(33), 7)
        self.assertEqual(normalize(-4), 22)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            normalize('a')
        with self.assertRaises(TypeError):
            normalize([])


class TestShiftForward(unittest.TestCase):
    # shift(int, int) -> int

    def test_shift(self):
        self.assertEqual(shift(2, 3), 5)
        self.assertEqual(shift(2, 26), 2)
        self.assertEqual(shift(2, 28), 4)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            shift('a', 2)
        with self.assertRaises(TypeError):
            shift(2, 'a')


class TestShiftBackward(unittest.TestCase):
    # shift_backwards(int, int) -> int

    def test_shift_backwards(self):
        self.assertEqual(shift_backwards(5, 3), 2)
        self.assertEqual(shift_backwards(2, 26), 2)
        self.assertEqual(shift_backwards(4, 28), 2)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            shift('a', 2)
        with self.assertRaises(TypeError):
            shift(2, 'a')


class TestOrderInAlphabet(unittest.TestCase):
    # order_in_alphabet(str) -> int

    def test_order_in_alphabet(self):
        self.assertEqual(order_in_alphabet('A'), 0)
        self.assertEqual(order_in_alphabet('C'), 2)
        self.assertEqual(order_in_alphabet('a'), 0)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            order_in_alphabet(4)

    def test_wrong_value(self):
        with self.assertRaises(ValueError):
            order_in_alphabet("ASD")


class TestShiftLetter(unittest.TestCase):
    # shift_letter(str, int) -> str

    def test_shift_letter(self):
        self.assertEqual(shift_letter('C', 3), 'F')
        self.assertEqual(shift_letter('A', 26), 'A')
        self.assertEqual(shift_letter('A', 28), 'C')

        self.assertEqual(shift_letter('c', 3), 'F')
        self.assertEqual(shift_letter('a', 26), 'A')
        self.assertEqual(shift_letter('a', 28), 'C')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            shift_letter(2, 2)
        with self.assertRaises(TypeError):
            shift_letter(2, 'a')

    def test_wrong_value(self):
        with self.assertRaises(ValueError):
            shift_letter('ad', 2)

    def test_shift_letter_backwards(self):
        self.assertEqual(shift_letter('E', -3), 'B')
        self.assertEqual(shift_letter('A', -26), 'A')
        self.assertEqual(shift_letter('C', -28), 'A')

        self.assertEqual(shift_letter('e', -3), 'B')
        self.assertEqual(shift_letter('a', -26), 'A')
        self.assertEqual(shift_letter('c', -28), 'A')


class TestToLetter(unittest.TestCase):
    # to_letter(int) -> str

    def test_order_in_alphabet(self):
        self.assertEqual(to_letter(0), 'A')
        self.assertEqual(to_letter(25), 'Z')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            to_letter('a')
        with self.assertRaises(TypeError):
            to_letter(2.3)


class TestPossibleShift(unittest.TestCase):
    # find_possible_shift(str, float) -> list

    def test_possible_shift(self):
        self.assertEqual(set(find_possible_shift('a', 7.5)),
                         set([0, 7, 9, 12, 13, 18]))
        self.assertEqual(set(find_possible_shift('c', 7.5)),
                         set([2, 9, 11, 14, 15, 20]))

    def test_wrong_value(self):
        with self.assertRaises(ValueError):
            find_possible_shift('ad', 2.0)


if __name__ == '__main__':
    unittest.main()
