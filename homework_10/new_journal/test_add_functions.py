import unittest
from unittest.mock import patch
from add_functions import distance


class TestDistLevenshtein(unittest.TestCase):
    """Тестирование Levenshtein distance"""
    def setUp(self):
        self.dist = distance

    def test_eq(self):
        """Тест одинаковыми словами"""
        for a, b in [['test', 'test'],
                     ['some_possible_long_string', 'some_possible_long_string']]:
            self.assertEqual(self.dist(a, b), 0)

    def test_zero_str(self):
        """Тест пустыми строками"""
        self.assertEqual(self.dist('', ''), 0)
        self.assertEqual(self.dist('qwerty', ''), 6)
        self.assertEqual(self.dist('', 'test'), 4)

    def test_reverse(self):
        """Тест полностью разными строками"""
        self.assertEqual(self.dist('test', 'some_possible_long_string'), 22)
        self.assertEqual(self.dist('some_possible_long_string', 'test'), 22)

    def test_add(self):
        """Тест с добавлением одной буквы"""
        self.assertEqual(self.dist('start', '_start'), 1)
        self.assertEqual(self.dist('middle', 'mid_dle'), 1)
        self.assertEqual(self.dist('end', 'end_'), 1)
        self.assertEqual(self.dist('several', 'sevekjral'), 2)  # рядом
        self.assertEqual(self.dist('several', 'seeveeral'), 2)  # в разных местах

    def test_delete(self):
        """Тест с удалением одной буквы"""
        self.assertEqual(self.dist('_start', 'start'), 1)
        self.assertEqual(self.dist('mid_dle', 'middle'), 1)
        self.assertEqual(self.dist('end_', 'end'), 1)
        self.assertEqual(self.dist('several', 'svral'), 2)
        self.assertEqual(self.dist('several', 'seral'), 2)

    def test_change(self):
        """Тест с изменением одной буквы"""
        self.assertEqual(self.dist('start', 'stirt'), 1)
        self.assertEqual(self.dist('middle', 'miydle'), 1)
        self.assertEqual(self.dist('end', 'enk'), 1)
        self.assertEqual(self.dist('several', 'sioeral'), 2)
        self.assertEqual(self.dist('several', 'sivoral'), 2)

