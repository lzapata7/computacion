from backgammon.core.player import Player
from backgammon.core.checker import Checker


def test_player_properties():
	p1 = Player("A", 1)
	p2 = Player("B", -1)
	assert p1.id() == 1 and p1.direction() == 1 and p1.home_range() == (18, 23)
	assert p2.id() == -1 and p2.direction() == -1 and p2.home_range() == (0, 5)


def test_checker_owner():
	c = Checker(1, 7)
	assert c.owner() == 1