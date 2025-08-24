import re
from backgammon.core.dice import Dice


def test_moves_from_roll_non_double():
	d = Dice()
	moves = d.moves_from_roll((3, 5))
	assert moves == [3, 5]


def test_moves_from_roll_double():
	d = Dice()
	moves = d.moves_from_roll((4, 4))
	assert moves == [4, 4, 4, 4]