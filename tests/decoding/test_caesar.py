import unittest
from decoding.caesar import (filter_keys, transform,
                             caesar_with_key, caesar)


class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.message = "We tell the word our secrets\
 in language it doesn't understand."
        self.encripted = "Zh whoo wkh zrug rxu vhfuhwv\
 lq odqjxdjh lw grhvq'w xqghuvwdqg."
        self.key = 3
        self.reversed_key = 23

    def test_filtering_keys(self):
        # filter_keys(str) -> [int]

        keys = filter_keys(self.message)
        self.assertLess(len(keys), 26)
        self.assertIn(self.reversed_key, keys)

    def test_transform_symbol(self):
        # transform(str, int) -> str

        self.assertEqual(transform('w', 3), 'Z')
        self.assertEqual(transform('z', 1), 'A')
        self.assertEqual(transform('9', 1), '9')
        self.assertEqual(transform('.', 1), '.')

    def test_caesar_with_key(self):
        # caesar_with_key(str, int) -> str

        self.assertEqual(caesar_with_key('', self.key), '')
        self.assertEqual(caesar_with_key('1223', self.key), '1223')
        self.assertEqual(caesar_with_key(self.message, self.key),
                         self.encripted.upper())
        self.assertEqual(caesar_with_key(self.encripted, self.reversed_key),
                         self.message.upper())

    def test_caesar(self):
        # caesar(str) -> [str]

        self.assertIn(self.message.upper(), caesar(self.encripted))


if __name__ == '__main__':
    unittest.main()
