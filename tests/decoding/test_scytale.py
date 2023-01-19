import unittest
from decoding.scytale import (scytale)


class TestScytaleCipher(unittest.TestCase):
    def setUp(self):
        self.message = "We tell the word our secrets\
 in language it doesn't understand."
        self.encripted = "WLORELADTRDETRSTAGOUS_THDE\
SNEENT_EEOCIGISDA_LWURNUTNEN_"
        self.turns = 5

    def test_scytale(self):
        # scytale(str) -> [str]
        pass
        # self.assertIn(self.message.upper(), scytale(self.encripted))


if __name__ == '__main__':
    unittest.main()
