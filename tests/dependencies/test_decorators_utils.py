import unittest
from dependencies.decorators_utils import type_of, is_type


class TestTypeOf(unittest.TestCase):
    def test_type_of_variables(self):
        self.assertEqual(type_of(5), int)
        self.assertEqual(type_of('a'), str)

    def test_type_of_types(self):
        self.assertEqual(type_of(int), int)
        self.assertEqual(type_of(str), str)
        self.assertEqual(type_of((int, [])), (int, []))

    def test_type_of_list(self):
        self.assertEqual(type_of([]), [])
        self.assertEqual(type_of([3, 2, 4]), [int])
        self.assertEqual(type_of(['a']), [str])
        self.assertEqual(type_of([[4]]), [[int]])
        self.assertEqual(type_of([[]]), [[]])

    def test_type_of_list_of_types(self):
        self.assertEqual(type_of([]), [])
        self.assertEqual(type_of([int]), [int])
        self.assertEqual(type_of([list]), [list])
        self.assertEqual(type_of([[int]]), [[int]])


class TestIsType(unittest.TestCase):
    def test_is_type(self):
        self.assertTrue(is_type(int, int))
        self.assertTrue(is_type([int], [int]))
        self.assertTrue(is_type([], [int]))
        self.assertTrue(is_type([int], []))
        self.assertTrue(is_type([[int]], [[int]]))
        self.assertTrue(is_type([[int]], [[]]))
        self.assertTrue(is_type([[]], [[int]]))
        self.assertTrue(is_type(str, ([], str)))
        self.assertTrue(is_type([], ([], str, int)))


if __name__ == '__main__':
    unittest.main()
