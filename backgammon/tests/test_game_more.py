from backgammon.core.game import BackgammonGame


def test_move_consumes_die_on_success_and_not_on_failure():
	g = BackgammonGame()
	# preparar estado determinista: una ficha P1 en 0 y destino vacío
	b = g.board()
	b.__points__ = [0] * 24
	b.__points__[0] = 1
	g.__moves_left__ = [1, 2]
	# movimiento válido
	ok = g.move(0, 1)
	assert ok is True
	assert g.moves_left() == [2]
	# movimiento inválido (usar dado inexistente)
	ok2 = g.move(1, 5)
	assert ok2 is False
	assert g.moves_left() == [2]


def test_move_requires_die_present():
	g = BackgammonGame()
	g.__moves_left__ = [3]
	# sin dado 2 debe fallar
	assert g.move(0, 2) is False


def test_can_move_any_with_bar_and_without():
	g = BackgammonGame()
	b = g.board()
	# Caso con barra: P1 tiene 1 en barra y puede entrar con die=1 en idx 0 abierto
	b.__bar__[1] = 1
	b.__points__[0] = 0
	g.__moves_left__ = [1]
	assert g.can_move_any(1) is True
	# Caso sin barra y con movimiento posible
	b.__bar__[1] = 0
	b.__points__ = [0] * 24
	b.__points__[0] = 1
	g.__moves_left__ = [1]
	assert g.can_move_any(1) is True


def test_end_turn_and_current_player_toggle():
	g = BackgammonGame()
	p1 = g.current_player().id()
	g.end_turn()
	p2 = g.current_player().id()
	assert p1 == 1 and p2 == -1
	g.end_turn()
	assert g.current_player().id() == 1


def test_winner_proxy_and_serialize():
	g = BackgammonGame()
	# Sin ganador
	assert g.winner() is None
	# Forzar ganador P1
	g.board().__born_off__[1] = 15
	assert g.winner() == 1
	s = g.serialize()
	assert isinstance(s["points"], list)
	assert isinstance(s["bar"], dict)
	assert isinstance(s["born_off"], dict)
	assert isinstance(s["moves_left"], list)