import unittest
from decoding.scytale import (scytale, find_bandwidth)


class TestScytaleCipher(unittest.TestCase):
    def setUp(self):
        self.message = "We tell the word our secrets\
 in language it doesn't understand."
        self.encripted = "Wled_eng_otenel__st_uie_rd\
__woeslatsus.ttouc_ag_nnt_ehrrrined'da_"
        self.turns = 5

    def test_find_bandwidth(self):
        # find_bandwidth(int) -> [int]

        self.assertIn(self.turns, find_bandwidth(len(self.encripted)))

    def test_scytale(self):
        # scytale(str) -> [(str, float)]

        self.assertIn(self.message,
                      [t[0] for t in scytale(self.encripted)])


if __name__ == '__main__':
    unittest.main()
