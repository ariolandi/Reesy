import unittest
from ..decorators_utils import *


class TestTypeOf(unittest.TestCase):
    def test_type_of_variables(self):
        self.assertEqual(type_of(5), int)
        self.assertEqual(type_of('a'), str)

    def test_type_of_types(self):
        self.assertEqual(type_of(int), int)
        self.assertEqual(type_of(str), str)

    def test_type_of_list(self):
        self.assertEqual(type_of([]), [])
        self.assertEqual(type_of([3, 2, 4]), [int])
        self.assertEqual(type_of(['a']), [str])

    def test_type_of_list_of_types(self):
        self.assertEqual(type_of([]), [])
        self.assertEqual(type_of([int]), [int])
        self.assertEqual(type_of([list]), [list])


class TestIsType(unittest.TestCase):
    def test_is_type(self):
        self.assertTrue(is_type(int, int))
        self.assertTrue(is_type([int], [int]))
        self.assertTrue(is_type([], [int]))
        self.assertTrue(is_type([int], []))


if __name__ == '__main__':
    unittest.main()
