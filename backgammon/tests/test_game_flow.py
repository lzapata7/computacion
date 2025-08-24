from backgammon.core.game import BackgammonGame


def test_roll_sets_moves():
	g = BackgammonGame()
	r = g.roll()
	assert len(g.moves_left()) in (2, 4)


def test_end_turn_clears_moves():
	g = BackgammonGame()
	g.roll()
	g.end_turn()
	assert g.moves_left() == []


def test_serialize_has_expected_keys():
	g = BackgammonGame()
	g.roll()
	s = g.serialize()
	for key in ["points", "bar", "born_off", "turn", "moves_left", "players"]:
		assert key in s