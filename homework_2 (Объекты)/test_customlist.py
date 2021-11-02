"""Тесты для CustomList"""

import unittest
from customlist import CustomList


# добавил тест типа возвращаемого значения
class TestCustomListReturnedType(unittest.TestCase):
    """Тест типа возвращаемого списка"""
    def setUp(self):
        self.a_list = CustomList([1, 2])
        self.b_list = CustomList([1, 3, 2])
        self.sim_list = [1, 3, 4]

    def test_type_add(self):
        """Сложение кастомных списков"""
        self.assertIsInstance(self.a_list + self.b_list, CustomList)
        self.assertIsInstance(self.b_list + self.a_list, CustomList)

    def test_type_add_list(self):
        """Сложение с обычным списком"""
        self.assertIsInstance(self.a_list + self.sim_list, CustomList)
        self.assertIsInstance(self.sim_list + self.a_list, CustomList)

    def test_type_sub(self):
        """Вычитание кастомных списков"""
        self.assertIsInstance(self.a_list - self.b_list, CustomList)
        self.assertIsInstance(self.b_list - self.a_list, CustomList)

    def test_type_add_list(self):
        """Вычитание с обычным списком"""
        self.assertIsInstance(self.sim_list - self.a_list, CustomList)
        self.assertIsInstance(self.a_list - self.sim_list, CustomList)


# добавил тест на неизменность исходных списков
class TestConstantlyCustomList(unittest.TestCase):
    """Тест на неизменность исходных списков"""
    def setUp(self):
        self.a_list = CustomList([1, 2])
        self.b_list = CustomList([1, 3, 4])
        self.sim_list = [1, 3, 4]

    def test_const_add(self):
        """Сложение кастомных списков"""
        self.a_list + self.b_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(list(self.b_list), [1, 3, 4])
        self.b_list + self.a_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(list(self.b_list), [1, 3, 4])

    def test_const_add_list(self):
        """Сложение с обычным списком"""
        self.a_list + self.sim_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(self.sim_list, [1, 3, 4])
        self.sim_list + self.a_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(self.sim_list, [1, 3, 4])

    def test_const_sub(self):
        """Вычитание кастомных списков"""
        self.a_list - self.b_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(list(self.b_list), [1, 3, 4])
        self.b_list - self.a_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(list(self.b_list), [1, 3, 4])

    def test_const_add_list(self):
        """Вычитание с обычным списком"""
        self.a_list - self.sim_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(self.sim_list, [1, 3, 4])
        self.sim_list - self.a_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.assertEqual(self.sim_list, [1, 3, 4])

    def test_const_equality(self):
        """Вычитание с обычным списком"""
        self.a_list == self.b_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.a_list >= self.b_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.a_list <= self.b_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.a_list > self.b_list
        self.assertEqual(list(self.a_list), [1, 2])
        self.a_list < self.b_list
        self.assertEqual(list(self.a_list), [1, 2])


# изменил на поэлементное равенство суммы/разности
class TestCustomListAdd(unittest.TestCase):
    """Тесты для СustomList (сложение)"""

    def test_add_custom_custom_equal(self):
        """[1, 2] + [1, 3] = [2, 5]"""
        a_list, b_list = CustomList([1, 2]), CustomList([1, 3])
        self.assertEqual(list(a_list + b_list), [2, 5])
        self.assertEqual(list(b_list + a_list), [2, 5])

    def test_add_custom_custom_not_equal(self):
        """[1, 2, 3] + [1, 2, 3, 4] = [2, 4, 6, 4]"""
        a_list, b_list = CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])
        self.assertEqual(list(a_list + b_list), [2, 4, 6, 4])
        self.assertEqual(list(b_list + a_list), [2, 4, 6, 4])

    def test_add_custom_list(self):
        """[1, 3] + list[1, 2, 4] = [2, 5, 4]"""
        custom_list, simple_list = CustomList([1, 3]), [1, 2, 4]
        self.assertEqual(list(custom_list + simple_list), [2, 5, 4])
        self.assertEqual(list(simple_list + custom_list), [2, 5, 4])


class TestCustomListSub(unittest.TestCase):
    """Тесты для СustomList (вычитание)"""

    def test_sub_custom_custom_equal(self):
        """
        [1, 2, 3] - [1, 4, 3] = [0, -2, 0]
        [1, 4, 3] - [1, 2, 3] = [0, 2, 0]
        """
        a_list, b_list = CustomList([1, 2, 3]), CustomList([1, 4, 3])
        self.assertEqual(list(a_list - b_list), [0, -2, 0])
        self.assertEqual(list(b_list - a_list), [0, 2, 0])

    def test_sub_custom_custom_not_equal(self):
        """
        [1, 2, 3] - [1, 2, 3, 4] = [0, 0, 0, -4]
        [1, 2, 3, 4] - [1, 2, 3] = [0, 0, 0, 4]
        """
        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])
        self.assertEqual(list(f_list - s_list), [0, 0, 0, -4])
        self.assertEqual(list(s_list - f_list), [0, 0, 0, 4])

    def test_sub_custom_list(self):
        """
        [1, 3] - list[1, 2, 4] = [0, 1, -4]
        list[1, 2, 4] - [1, 3] = [0, -1, 4]
        """
        custom_list, simple_list = CustomList([1, 3]), [1, 2, 4]
        self.assertEqual(list(custom_list - simple_list), [0, 1, -4])
        self.assertEqual(list(simple_list - custom_list), [0, -1, 4])


class TestCustomListEquality(unittest.TestCase):
    """Тесты для СustomList (равенства)"""

    def test_eq(self):
        """
        [1, 2, 3] == [1, 2, 3] => True
        [1, 2, 3] == [1, 2, 4] => False
        [1, 3, 2] == [1, 2, 3] => True
        """
        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 2, 3])
        self.assertTrue(f_list == s_list)

        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 2, 4])
        self.assertFalse(f_list == s_list)

        f_list, s_list = CustomList([1, 3, 2]), CustomList([1, 2, 3])
        self.assertTrue(f_list == s_list)

    def test_ne(self):
        """
        [1, 2, 3] != [1, 2, 3] => False
        [1, 2, 3] != [1, 2, 4] => True
        [1, 3, 2] != [1, 2, 3] => False
        """
        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 2, 3])
        self.assertFalse(f_list != s_list)

        f_list, s_list = CustomList([1, 2, 3]), CustomList([1, 2, 4])
        self.assertTrue(f_list != s_list)

        f_list, s_list = CustomList([1, 3, 2]), CustomList([1, 2, 3])
        self.assertFalse(f_list != s_list)

    def test_gt(self):
        """
        [2] > [1] => True
        [1] > [2] => False
        [2] > [2] => False
        """
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertTrue(f_list > s_list)
        self.assertFalse(s_list > f_list)

    def test_lt(self):
        """
        [2] < [1] => False
        [1] < [2] => True
        [2] < [2] => False
        """
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertFalse(f_list < s_list)
        self.assertTrue(s_list < f_list)

    def test_ge(self):
        """
        [2] >= [1] => True
        [1] >= [2] => False
        [2] >= [2] => True
        """
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertTrue(f_list >= s_list)
        self.assertFalse(s_list >= f_list)

    def test_le(self):
        """
        [2] <= [1] => False
        [1] <= [2] => True
        [2] <= [2] => True
        """
        f_list, s_list = CustomList([2]), CustomList([1])
        self.assertFalse(f_list <= s_list)
        self.assertTrue(s_list <= f_list)
