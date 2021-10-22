"""
	Игра крестики-нолики
"""

import os
from combinations import combinations


class TicTacGame:
    """Класс игры крестики-нолики"""

    def __init__(self):
        self.count = 3
        self.players = {0: ['player1', 'o'], 1: ['player2', '+']}
        self.board = {i: i for i in range(1, self.count ** 2 + 1)}

    def input_name(self, text):
        """Проверка на ввод имени игрока
            Вывод: валидное имя игрока"""
        name = input(text)
        if name.isalpha():
            return name
        print("Извините, можно использовать только буквы. Повторите ввод имени: ")
        return self.input_name(text)

    def start_game(self):
        """Старт игры"""
        for i, player in self.players.items():
            text = f'Введите имя {i + 1}-ого игрока: '
            player[0] = self.input_name(text)

        current_ind = 0
        next_ind = 1
        while self.check_winner() is None:
            os.system('cls')
            print(f'Ход игрока - {self.players[current_ind][0]}')
            self.show_board()
            self.step(current_ind)
            current_ind, next_ind = next_ind, current_ind

        os.system('cls')
        self.show_board()
        print(f'WINNER - {self.check_winner()}  !!!')

    def step(self, ind):
        """Ход игрока"""
        num = input("Введите координату: ")
        if self.validate_input(num):
            self.board[int(num)] = self.players[ind][1]
        else:
            self.step(ind)

    def show_board(self):
        """Вывод игрового поля"""
        print("Рабочее поле:")
        print('\t' + '---' * self.count)
        string = []
        for key, value in self.board.items():
            string.append(value)
            if key % 3 == 0:
                print('\t' + ' | '.join(map(str, string)))
                print('\t' + '---' * self.count)
                string = []

    def validate_input(self, num):
        """Проверка ввода координаты
            Вывод: True - если знач. валидно"""
        if not num.isdigit():
            print('Вы ввели не число')
            return False
        if not 1 <= int(num) <= self.count ** 2:
            print('Число превысила допустимые пределы')
            return False
        if not isinstance(self.board[int(num)], int):
            print('Это поле уже занято')
            return False
        return True

    def check_winner(self):
        """Проверка на присутствие победителя или ничьи"""
        # проверка выигрывающих комбинаций
        for name, sign in self.players.values():
            for arg1, arg2, arg3 in combinations:
                if self.board[arg1] == self.board[arg2] == self.board[arg3] == sign:
                    return name

        # проверка на ничью
        flag = True
        for k in self.board.keys():
            if self.board[k] == k:
                flag = False
        if flag:
            return 'IS MISSING (Победитель отсутствует)'

        return None


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
