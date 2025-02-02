#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test class for max_integer"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_identical_numbers(self):
        """Test with identical numbers"""
        self.assertEqual(max_integer([8, 8, 8, 8]), 8)

    def test_max_at_beginning(self):
        """Test with maximum at beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_at_middle(self):
        """Test with maximum in middle"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_max_at_end(self):
        """Test with maximum at end"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([999999, 1000000, 999998]), 1000000)

    def test_zero(self):
        """Test with zero in list"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_big_list(self):
        """Test with a big list"""
        self.assertEqual(max_integer(list(range(100)) + [100] + list(range(101, 200))), 199)

    def test_string_list(self):
        """Test with list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_invalid_types(self):
        """Test with invalid types in list"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 2, 3])
        with self.assertRaises(TypeError):
            max_integer([1, None, 2])


if __name__ == '__main__':
    unittest.main()
