"""Тесты для CustomMeta"""

import unittest

from metaclass import CustomMeta


class TestCustomClass(metaclass=CustomMeta):
    """Тестовый класс класс"""
    x = 50

    def __init__(self, val=99):
        # print('CLASS INIT')
        self.val = val

    def line(self):
        """Test func return: 100"""
        return 100

    def line_val(self):
        """Test func return: custom_val+100"""
        return self.custom_val + 100


class TestCustomMeta(unittest.TestCase):
    """Тесты"""
    def setUp(self):
        self.inst = TestCustomClass()

    def test_magic_methods(self):
        """Тест magic методов"""
        for name in dir(self.inst):
            if not name.startswith('__') or not name.endswith('__'):
                self.assertEqual(name.split('_')[0], 'custom')

    def test_attr(self):
        """Тест изменения аттрибута класса"""
        self.assertEqual(self.inst.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.inst.x

    def test_func_line(self):
        """Тест изменения функций класса"""
        self.assertEqual(self.inst.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.inst.line()

    def test_func_line_val(self):
        """Тест изменения аттрибута экземпляра"""
        self.assertEqual(self.inst.custom_line_val(), 199)
        with self.assertRaises(AttributeError):
            self.inst.line_val()

    def test_attr_init_val(self):
        """Тест изменения аттрибута экземпляра"""
        self.assertEqual(self.inst.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.inst.val
