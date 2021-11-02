"""
    Тестирование
"""

import unittest
from unittest.mock import patch
from main import TicTacGame
from combinations import start_board


class TestTicTacGame(unittest.TestCase):
    """Тесты игры в крестики-нолики"""
    def setUp(self):
        self.game = TicTacGame()

    def test_validate_input(self):
        """Тест правильного ввода"""
        for i in range(1, self.game.count + 1):
            self.assertTrue(self.game.validate_input(str(i)))

# добавил проверку при вводе во время игры букв
    @patch('builtins.print')
    def test_invalidate_input(self, _):
        """Тест неправильного ввода"""
        for i in [-1, 0, self.game.count ** 2 + 1, self.game.count ** 2 * 2, 'c', 'str']:
            self.assertFalse(self.game.validate_input(str(i)))

# добавил проверку на свободную или занятую клетку
    @patch('builtins.print')
    def test_repeated_input(self, _):
        """
        Проверка на ввод уже занятой клетки и свободной клетки
        o | x | 3
        4 | 5 | 6
        7 | 8 | 9
        """
        self.game.board = start_board(self.game.count)
        self.game.board[1] = 'o'
        self.game.board[2] = 'x'
        self.assertFalse(self.game.validate_input('1'))
        self.assertFalse(self.game.validate_input('2'))
        self.assertTrue(self.game.validate_input('3'))

    def test_check_winner(self):
        """Тест на проверку чьей то победы"""
        test_combinations = []
        self._make_test_combinations(test_combinations)
        for text_comb, win in test_combinations:
            self.game.board = text_comb
            self.assertEqual(self.game.check_winner(), win)

# упростил для понимания
    def _make_test_combinations(self, test):
        new_board = start_board(self.game.count)
        """
        1 | 2 | 3
        4 | 5 | 6
        7 | 8 | 9
        """
        test.append((new_board, None))
        """
        o | o | o
        4 | 5 | 6
        7 | 8 | 9
        """
        board = new_board.copy()
        board[1] = 'o'
        board[2] = 'o'
        board[3] = 'o'
        test.append((board, 'player1'))
        """
        1 | o | 3
        4 | o | 6
        7 | o | 9
        """
        board = new_board.copy()
        board[2] = 'o'
        board[5] = 'o'
        board[8] = 'o'
        test.append((board, 'player1'))
        """
        + | 2 | 3
        4 | + | 6
        7 | 8 | +
        """
        board = new_board.copy()
        board[1] = '+'
        board[5] = '+'
        board[9] = '+'
        test.append((board, 'player2'))
        """
        1 | 2 | +
        4 | + | 6
        + | 8 | 9
        """
        board = new_board.copy()
        board[3] = '+'
        board[5] = '+'
        board[7] = '+'
        test.append((board, 'player2'))
        """
        1 | 2 | o
        4 | 5 | o
        7 | 8 | o
        """
        board = new_board.copy()
        board[3] = 'o'
        board[6] = 'o'
        board[9] = 'o'
        test.append((board, 'player1'))
        """
        o | + | +
        + | o | o
        o | + | +
        """
        test.append(({1: 'o', 2: '+', 3: '+', 4: '+', 5: 'o', 6: 'o', 7: 'o', 8: '+', 9: '+'},
                     'IS MISSING (Победитель отсутствует)'))


if __name__ == '__main__':
    unittest.main()
