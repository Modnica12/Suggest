import unittest
from sug import suggest


class TestSuggest(unittest.TestCase):
    # def test_abakanets(self):
    #    sug = suggest.Suggester("ruwords.txt")
    #    res = sug.get('аб')
    #    # print(res)
    #    self.assertEqual("абаканец\n" in res, True)

    def test_count(self):
        sug = suggest.Suggester("ruwords.txt")
        res = sug.get('при')

        self.assertEqual(len(res), suggest.MAX_FOUND)

    def test_t(self):
        sug = suggest.Suggester("ruwords.txt")
        res = sug.get('а')

        print(res)

        self.assertEqual(len(res), suggest.MAX_FOUND)
