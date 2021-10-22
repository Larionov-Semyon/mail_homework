"""
    Тестирование
"""

import unittest
from unittest.mock import patch
from main import TicTacGame


class TestTicTacGame(unittest.TestCase):
    """Тесты игры в крестики-нолики"""
    def setUp(self):
        self.game = TicTacGame()

# нет буквенной проверки ввода
    def test_validate_input(self):
        """Тест правильного ввода имени игрока"""
        for i in range(1, self.game.count + 1):
            self.assertTrue(self.game.validate_input(str(i)))

    @patch('builtins.print')
    def test_invalidate_input(self, _):
        """Тест неправильного ввода имени игрока"""
        for i in [-1, 0, self.game.count ** 2 + 1, self.game.count ** 2 * 2]:
            self.assertFalse(self.game.validate_input(str(i)))

    def test_check_winner(self):
        """Тест на проверку чьей то победы"""
        test_combinations = []
        self._make_test_combinations(test_combinations)
        for text_comb, win in test_combinations:
            self.game.board = text_comb
            self.assertEqual(self.game.check_winner(), win)

# слишком сложно для понимания
    @classmethod
    def _make_test_combinations(cls, test):
        test.append(({i: i for i in range(1, 10)}, None))
        test.append(({i: i if not (i in (1, 2, 3)) else 'o' for i in range(1, 10)}, 'player1'))
        test.append(({i: i if not (i in (2, 5, 8)) else 'o' for i in range(1, 10)}, 'player1'))
        test.append(({i: i if not (i in (1, 5, 9)) else '+' for i in range(1, 10)}, 'player2'))
        test.append(({i: i if not (i in (3, 5, 7)) else '+' for i in range(1, 10)}, 'player2'))
        test.append(({i: i if not (i in (3, 6, 9)) else 'o' for i in range(1, 10)}, 'player1'))
        test.append(({1: 'o', 2: '+', 3: '+', 4: 'x', 5: 'o', 6: 'o', 7: 'o', 8: '+', 9: '+'},
                     'IS MISSING (Победитель отсутствует)'))


if __name__ == '__main__':
    unittest.main()
