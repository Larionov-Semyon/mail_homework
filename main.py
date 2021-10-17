import os


class TicTacGame:
	n = 3

	def __init__(self):
		self.player1 = input('Введите имя 1-ого игрока: ')
		self.player2 = input('Введите имя 2-ого игрока: ')
		self.players = {0: (self.player1, 'o'), 1: (self.player2, '+')}
		self.board = {i: i for i in range(1, self.n**2 + 1)}

	def start_game(self):
		current_ind = 0
		next_ind = 1
		while self.check_winner() is None:
			os.system('cls')
			self.step(current_ind)
			current_ind, next_ind = next_ind, current_ind

		os.system('cls')
		self.show_board()
		print("WIN - " + self.check_winner())

	def step(self, ind):
		print("Ход игрока - {}".format(self.players[ind][0]))
		self.show_board()
		x = int(input("Введите координату: "))
		if self.validate_input(x):
			self.board[x] = self.players[ind][1]
		else:
			os.system('cls')
			print("Это поле уже занято")
			self.step(ind)

	def show_board(self):
		print("Рабочее поле:")
		print("---" * self.n)
		l = []
		for k, v in self.board.items():
			l.append(v)
			if k % 3 == 0:
				print(' | '.join(map(str, l)))
				l = []
				print("---" * self.n)

	def validate_input(self, x):
		return isinstance(self.board[x], int)

	def check_winner(self):
		for name, sign in self.players.values():
			l = []
			for k, v in self.board.items():
					l.append(v)
					if k % 3 == 0:
						if l == [sign] * self.n:
							return name
						l = []
			l = []
			for x in range(1, self.n + 1):
				for y in range(self.n):
					l.append(self.board[x + y * 3])
				if l == [sign] * self.n:
					return name

			if self.board[1] == self.board[5] == self.board[9] == sign:
				return name
			if self.board[3] == self.board[5] == self.board[7] == sign:
				return name

		return None


if __name__ == '__main__':
	game = TicTacGame()
	game.start_game()
