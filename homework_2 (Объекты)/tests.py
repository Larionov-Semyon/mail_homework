import unittest

from main import CustomList


class TestCustomList(unittest.TestCase):
    """Тесты"""
    def _test_add_reverse(self, f_list, s_list, ans):
        self.assertEqual(f_list + s_list, ans)
        self.assertEqual(s_list + f_list, ans)

    def test_add_custom_custom(self):
        self._test_add_reverse(CustomList([1, 2]), CustomList([1, 3]), CustomList([2, 5]))
        self._test_add_reverse(CustomList([1, 2, 3]), CustomList([1, 2, 3, 4]), CustomList([2, 4, 6, 4]))

    def test_sub_custom_custom(self):
        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 4, 3])
        self.assertEqual(f_list - s_list, CustomList([0, -2, 0]))
        self.assertEqual(s_list - f_list, CustomList([0, 2, 0]))

        long_list = CustomList([1, 2, 3, 4])
        self.assertEqual(f_list - long_list, CustomList([0, 0, 0, -4]))
        self.assertEqual(long_list - f_list, CustomList([0, 0, 0, 4]))

    def test_add_custom_list(self):
        custom_list, simple_list = CustomList([1, 3]), [1, 2, 4]
        self.assertEqual(custom_list - simple_list, CustomList([0, 1, -4]))
        self.assertEqual(simple_list - custom_list, CustomList([0, -1, 4]))

    def test_eq(self):
        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 2, 3])
        self.assertTrue(f_list == s_list)

        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 2, 4])
        self.assertFalse(f_list == s_list)

        f_list, s_list = CustomList([1, 3, 2]), CustomList([1, 2, 3])
        self.assertTrue(f_list == s_list)

    def test_gt(self):
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertTrue(f_list > s_list)
        self.assertFalse(s_list > f_list)
        self.assertFalse(s_list > s_list)

    def test_lt(self):
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertFalse(f_list < s_list)
        self.assertTrue(s_list < f_list)
        self.assertFalse(s_list < s_list)

    def test_ge(self):
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertTrue(f_list >= s_list)
        self.assertFalse(s_list >= f_list)
        self.assertTrue(s_list >= s_list)

    def test_le(self):
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertFalse(f_list <= s_list)
        self.assertTrue(s_list <= f_list)
        self.assertTrue(s_list <= s_list)
