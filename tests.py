import os
import unittest

import lzf


class LZFTest(object):
    def compress(self, text):
        # lzf guarantees that even if the compressed version is longer, it is
        # within 104% of the original size (rounded up), so this should work
        return lzf.compress(text, len(text) * 2)

    def test_selective(self):
        compressed = self.compress(self.VAL)
        self.assertEqual(lzf.decompress(compressed, len(self.VAL) - 1), None)
        assert lzf.decompress(compressed, len(self.VAL))

    def test_decompresses_correctly(self):
        compressed = self.compress(self.VAL)
        self.assertEqual(lzf.decompress(compressed, len(self.VAL)), self.VAL)


class ShortString(LZFTest, unittest.TestCase):
    VAL = "this is a test"

class StringWithRepetition(LZFTest, unittest.TestCase):
    VAL = "a longer string, repeating. " * 500

class LongStringNoRepetition(LZFTest, unittest.TestCase):
    VAL = open(os.path.join(os.path.dirname(__file__), "lzf_module.c")).read()