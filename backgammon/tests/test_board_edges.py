from backgammon.core.board import Board


def test_invalid_move_out_of_bounds():
	b = Board()
	b.__points__ = [0] * 24
	b.__points__[23] = 1
	# mover P1 23 + 6 -> con todas las fichas en casa, overshoot permitido
	assert b.apply_move(1, 23, 6) is True


def test_is_point_open_for_both_players_single_opponent():
	b = Board()
	b.__points__ = [0] * 24
	b.__points__[4] = -1
	assert b.is_point_open(1, 4) is True
	b.__points__[5] = 1
	assert b.is_point_open(-1, 5) is True


def test_cannot_bear_off_when_bar_has_checkers():
	b = Board()
	b.__points__ = [0] * 24
	b.__points__[23] = 1
	b.__bar__[1] = 1
	assert b.apply_move(1, 23, 1) is False