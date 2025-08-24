from backgammon.core.board import Board


def test_cannot_move_when_bar_has_checkers():
	b = Board()
	b.__bar__[1] = 1
	# intentar mover desde 0 con die 1 debe fallar porque debe entrar desde barra
	assert b.apply_move(1, 0, 1) is False


def test_blocked_destination():
	b = Board()
	# preparar una ficha P1 en 0 y destino 1 bloqueado por P2 con -2
	b.__points__ = [0] * 24
	b.__points__[0] = 1
	b.__points__[1] = -2
	assert b.apply_move(1, 0, 1) is False


def test_move_from_bar_p2_blocked_then_allowed():
	b = Board()
	b.__bar__[-1] = 1
	# die=1 entra a 23 para P2; bloqueado si hay +2
	b.__points__[23] = 2
	assert b.move_from_bar(-1, 1) is False
	# liberar punto
	b.__points__[23] = 0
	assert b.move_from_bar(-1, 1) is True
	assert b.bar(-1) == 0


def test_bearing_off_requires_all_in_home():
	b = Board()
	# P1 con una ficha fuera de casa
	b.__points__ = [0] * 24
	b.__points__[10] = 1
	b.__points__[23] = 1
	# intentar salir desde 23 con die=1 debe fallar
	assert b.apply_move(1, 23, 1) is False


def test_winner_after_bear_off():
	b = Board()
	b.__born_off__[1] = 15
	assert b.winner() == 1