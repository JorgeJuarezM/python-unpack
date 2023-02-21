import unittest
import unpack


class TestCase(unittest.TestCase):
    """Test unpack values."""

    def test_unpack_dict(self):
        a = unpack.from_dict({"a": 1})
        b, c = unpack.from_dict({"b": 2, "c": 3})
        self.assertEqual(a, 1, "Should be 1")
        self.assertEqual(b, 2, "Should be 2")
        self.assertEqual(c, 3, "Should be 3")

