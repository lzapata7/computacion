import pytest
from backgammon.core.dice import Dice


def test_moves_from_roll_without_roll_raises():
	d = Dice()
	with pytest.raises(ValueError):
		_ = d.moves_from_roll(None)