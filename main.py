import os
from combinations import combinations


class TicTacGame:
	n = 3

	def __init__(self):
		self.player1 = self.input_name('Введите имя 1-ого игрока: ')
		self.player2 = self.input_name('Введите имя 2-ого игрока: ')
		self.players = {0: (self.player1, 'o'), 1: (self.player2, '+')}
		self.board = {i: i for i in range(1, self.n**2 + 1)}

	def input_name(self, text):
		"""Проверка на ввод имени игрока
			Вывод: валидное имя игрока"""
		name = input(text)
		if name.isalpha():
			return name
		else:
			print("Извините, можно использовать только буквы. Повторите ввод имени: ")
			return self.input_name(text)

	def start_game(self):
		"""Игра"""
		current_ind = 0
		next_ind = 1
		while self.check_winner() is None:
			os.system('cls')
			print("Ход игрока - {}".format(self.players[current_ind][0]))
			self.show_board()
			self.step(current_ind)
			current_ind, next_ind = next_ind, current_ind

		os.system('cls')
		self.show_board()
		print("WINNER - {}  !!!".format(self.check_winner()))

	def step(self, ind):
		"""Ход игрока"""
		x = input("Введите координату: ")
		if self.validate_input(x):
			self.board[int(x)] = self.players[ind][1]
		else:
			self.step(ind)

	def show_board(self):
		"""Вывод игрового поля"""
		print("Рабочее поле:")
		print('\t' + '---' * self.n)
		string = []
		for k, v in self.board.items():
			string.append(v)
			if k % 3 == 0:
				print('\t' + ' | '.join(map(str, string)))
				print('\t' + '---' * self.n)
				string = []

	def validate_input(self, x):
		"""Проверка ввода координаты
			Вывод: True - если знач. валидно"""
		if not x.isdigit():
			print('Вы ввели не число')
			return False
		elif not 1 <= int(x) <= self.n**2:
			print('Число превысила допустимые пределы')
			return False
		elif not isinstance(self.board[int(x)], int):
			print('Это поле уже занято')
			return False
		else:
			return True

	def check_winner(self):
		"""Проверка на присутствие победителя или ничьи"""
		# проверка выигрывающих комбинаций
		for name, sign in self.players.values():
			for x, y, z in combinations:
				if self.board[x] == self.board[y] == self.board[z] == sign:
					return name
		# проверка на ничью
		b = True
		for k in self.board.keys():
			if self.board[k] == k:
				b = False
		if b:
			return 'IS MISSING (Победитель отсутствует)'

		return None


if __name__ == '__main__':
	game = TicTacGame()
	game.start_game()
