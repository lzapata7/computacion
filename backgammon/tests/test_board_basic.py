from backgammon.core.board import Board


def test_initial_setup_counts():
	b = Board()
	assert sum(v for v in b.points() if v > 0) == 15
	assert -sum(v for v in b.points() if v < 0) == 15


def test_is_point_open_rules():
	b = Board()
	# point 0 tiene -2, no está abierto para P1
	assert b.is_point_open(1, 0) is False
	# point 23 tiene +2, no está abierto para P2
	assert b.is_point_open(-1, 23) is False


def test_hit_on_single_checker():
	b = Board()
	# Crear situación de un solo checker enemigo en 4 y mover P1 desde 0.. simulación
	b.__points__[4] = -1
	b.__points__[0] = 0
	b.__points__[1] = 1  # P1 en 1
	ok = b.apply_move(1, 1, 3)  # 1->4
	assert ok is True
	assert b.bar(-1) == 1
	assert b.points()[4] > 0


def test_enter_from_bar():
	b = Board()
	b.__bar__[1] = 1
	# entrada con dado 1 a punto 0 (bloqueado por -2 en setup)
	assert b.move_from_bar(1, 1) is False
	# despejamos el punto 0
	b.__points__[0] = 0
	assert b.move_from_bar(1, 1) is True
	assert b.bar(1) == 0