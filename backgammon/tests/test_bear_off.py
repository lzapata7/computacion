from backgammon.core.board import Board


def prepare_home_for_p1(board: Board):
	# Mover todas las fichas de P1 a casa [18..23]
	board.__points__ = [0] * 24
	board.__points__[18] = 2
	board.__points__[19] = 3
	board.__points__[20] = 4
	board.__points__[21] = 3
	board.__points__[22] = 2
	board.__points__[23] = 1


def test_bear_off_p1_exact_and_overshoot():
	b = Board()
	prepare_home_for_p1(b)
	# Exacto desde 23 con die=1
	assert b.apply_move(1, 23, 1) is True
	# Overshoot permitido si no hay fichas más allá
	# desde 22 con die=3: distance=2, die>distance pero no hay más allá (en 23 ya se retiró)
	assert b.apply_move(1, 22, 3) is True


def prepare_home_for_p2(board: Board):
	board.__points__ = [0] * 24
	board.__points__[5] = -2
	board.__points__[4] = -3
	board.__points__[3] = -4
	board.__points__[2] = -3
	board.__points__[1] = -2
	board.__points__[0] = -1


def test_bear_off_p2_exact_and_overshoot():
	b = Board()
	prepare_home_for_p2(b)
	assert b.apply_move(-1, 0, 1) is True
	assert b.apply_move(-1, 1, 3) is True