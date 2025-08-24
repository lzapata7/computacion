from backgammon.core.board import Board


def test_has_all_in_home_checks_bar_and_positions():
	b = Board()
	# P1: bar > 0 -> False
	b.__bar__[1] = 1
	assert b.has_all_in_home(1) is False
	b.__bar__[1] = 0
	# P2: bar > 0 -> False
	b.__bar__[-1] = 1
	assert b.has_all_in_home(-1) is False
	b.__bar__[-1] = 0
	# P2: una ficha fuera de casa (>5) -> False
	b.__points__ = [0] * 24
	b.__points__[10] = -1
	assert b.has_all_in_home(-1) is False


def test_apply_hit_for_player_minus_one():
	b = Board()
	b.__points__ = [0] * 24
	b.__points__[5] = -1
	b.__points__[4] = 1  # single opponent
	# mover P2 desde 5 con die=1 a 4, debería capturar
	ok = b.apply_move(-1, 5, 1)
	assert ok is True
	assert b.bar(1) == 1
	assert b.points()[4] < 0


def test_move_from_bar_when_empty_fails():
	b = Board()
	assert b.move_from_bar(1, 1) is False


def test_has_checkers_beyond_true_paths():
	b = Board()
	b.__points__ = [0] * 24
	b.__points__[20] = 1
	assert b._has_checkers_beyond(1, 18) is True
	b.__points__ = [0] * 24
	b.__points__[2] = -1
	assert b._has_checkers_beyond(-1, 4) is True


def test_apply_move_from_none_without_bar_returns_false():
	b = Board()
	b.__bar__[1] = 0
	assert b.apply_move(1, None, 1) is False


def test_apply_move_wrong_owner_returns_false():
	b = Board()
	b.__points__ = [0] * 24
	# P1 intenta mover donde no tiene ficha
	assert b.apply_move(1, 0, 1) is False
	# P2 intenta mover donde hay ficha P1
	b.__points__[0] = 1
	assert b.apply_move(-1, 0, 1) is False


def test_winner_for_player_minus_one():
	b = Board()
	b.__born_off__[-1] = 15
	assert b.winner() == -1