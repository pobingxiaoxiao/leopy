from unittest import TestCase
import leopy

class TestText(TestCase):
    def test_is_string(self):
        s = leopy.joke()
        self.assertTrue(isinstance(s, str))