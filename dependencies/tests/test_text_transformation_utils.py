import unittest
from ..text_transformation_utils import *


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
    # shift_forward(int, int) -> int

    def test_shift_forward(self):
        self.assertEqual(shift_forward(2, 3), 5)
        self.assertEqual(shift_forward(2, 26), 2)
        self.assertEqual(shift_forward(2, 28), 4)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            shift_forward('a', 2)
        with self.assertRaises(TypeError):
            shift_forward(2, 'a')


class TestShiftBackward(unittest.TestCase):
    # shift_back(int, int) -> int

    def test_shift_backward(self):
        self.assertEqual(shift_backward(5, 3), 2)
        self.assertEqual(shift_backward(2, 26), 2)
        self.assertEqual(shift_backward(4, 28), 2)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            shift_backward('a', 2)
        with self.assertRaises(TypeError):
            shift_backward(2, 'a')


class TestOrderInAlphabet(unittest.TestCase):
    # order_in_alphabet(str) -> int

    def test_order_in_alphabet(self):
        self.assertEqual(order_in_alphabet('A'), 0)
        self.assertEqual(order_in_alphabet('C'), 2)
        self.assertEqual(order_in_alphabet('a'), 0)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            order_in_alphabet(4)
        with self.assertRaises(TypeError):
            order_in_alphabet("ASD")


class TestShiftLetterForward(unittest.TestCase):
    # shift_letter_forward(str, int) -> str

    def test_shift_letter_forward(self):
        self.assertEqual(shift_letter_forward('C', 3), 'F')
        self.assertEqual(shift_letter_forward('A', 26), 'A')
        self.assertEqual(shift_letter_forward('A', 28), 'C')

        self.assertEqual(shift_letter_forward('c', 3), 'F')
        self.assertEqual(shift_letter_forward('a', 26), 'A')
        self.assertEqual(shift_letter_forward('a', 28), 'C')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            shift_letter_forward(2, 2)
        with self.assertRaises(TypeError):
            shift_letter_forward(2, 'a')


class TestShiftLetterBackward(unittest.TestCase):
    # shift_back(str, int) -> str

    def test_shift_letter_backward_letter(self):
        self.assertEqual(shift_letter_backward('E', 3), 'B')
        self.assertEqual(shift_letter_backward('A', 26), 'A')
        self.assertEqual(shift_letter_backward('C', 28), 'A')

        self.assertEqual(shift_letter_backward('e', 3), 'B')
        self.assertEqual(shift_letter_backward('a', 26), 'A')
        self.assertEqual(shift_letter_backward('c', 28), 'A')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            shift_letter_backward(2, 2)
        with self.assertRaises(TypeError):
            shift_letter_backward(2, 'a')


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
    # find_possible_shift(str, float):

    def test_possible_shift(self):
        self.assertEqual(set(find_possible_shift('a', 7.5)), set([0, 7, 9, 12, 13, 18]))
        self.assertEqual(set(find_possible_shift('c', 7.5)), set([2, 9, 11, 14, 15, 20]))


if __name__ == '__main__':
    unittest.main()
