import unittest

from metaclass import CustomClass


class TestCustomClass(unittest.TestCase):
    """Тесты"""
    def setUp(self):
        self.inst = CustomClass()

    def test(self):
        print(dir(self.inst))
        for name in dir(self.inst):
            if not name.startswith('__'):
                print(name)
                self.assertTrue(name.split('_')[0] == 'custom')