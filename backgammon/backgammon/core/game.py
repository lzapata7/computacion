from __future__ import annotations
from typing import List, Optional, Tuple

from .board import Board
from .dice import Dice
from .player import Player


class BackgammonGame:
	"""Coordina el flujo del juego.

	Atributos:
	- __board__: instancia de Board
	- __dice__: instancia de Dice
	- __players__: lista [Player(1), Player(-1)]
	- __turn__: índice del jugador actual (0 para id=1, 1 para id=-1)
	- __moves_left__: lista de dados restantes a jugar
	"""

	def __init__(self, player1_name: str = "Jugador 1", player2_name: str = "Jugador 2") -> None:
		self.__board__ = Board()
		self.__dice__ = Dice()
		self.__players__ = [Player(player1_name, 1), Player(player2_name, -1)]
		self.__turn__ = 0
		self.__moves_left__: List[int] = []

	def board(self) -> Board:
		return self.__board__

	def current_player(self) -> Player:
		return self.__players__[self.__turn__]

	def opponent(self) -> Player:
		return self.__players__[1 - self.__turn__]

	def roll(self) -> Tuple[int, int]:
		roll = self.__dice__.roll()
		self.__moves_left__ = self.__dice__.moves_from_roll(roll)
		return roll

	def moves_left(self) -> List[int]:
		return list(self.__moves_left__)

	def _consume_move_value(self, used: int) -> bool:
		try:
			self.__moves_left__.remove(used)
			return True
		except ValueError:
			return False

	def can_move_any(self, player_id: int) -> bool:
		# Verifica si hay algún movimiento posible con los dados restantes
		if self.__board__.bar(player_id) > 0:
			for die in sorted(set(self.__moves_left__), reverse=True):
				if self.__board__.can_enter_from_bar(player_id, die):
					return True
			return False
		# Buscar desde todos los puntos (simulación sobre copia)
		for idx, val in enumerate(self.__board__.points()):
			if player_id == 1 and val > 0:
				for die in sorted(set(self.__moves_left__), reverse=True):
					bcopy = self.__board__.copy()
					if bcopy.apply_move(1, idx, die):
						return True
			elif player_id == -1 and val < 0:
				for die in sorted(set(self.__moves_left__), reverse=True):
					bcopy = self.__board__.copy()
					if bcopy.apply_move(-1, idx, die):
						return True
		return False

	def move(self, from_idx: Optional[int], die: int) -> bool:
		"""Realiza un movimiento del jugador actual.

		Devuelve True si se ejecutó y consume el dado.
		"""
		player = self.current_player().id()
		if die not in self.__moves_left__:
			return False
		board_before = self.__board__.copy()
		ok = self.__board__.apply_move(player, from_idx, die)
		if not ok:
			return False
		# Consumo preferente del valor exacto; para dobles es indistinto
		self._consume_move_value(die)
		return True

	def end_turn(self) -> None:
		self.__turn__ = 1 - self.__turn__
		self.__moves_left__.clear()

	def winner(self) -> Optional[int]:
		return self.__board__.winner()

	def serialize(self) -> dict:
		return {
			"points": self.__board__.points(),
			"bar": {1: self.__board__.bar(1), -1: self.__board__.bar(-1)},
			"born_off": {1: self.__board__.born_off(1), -1: self.__board__.born_off(-1)},
			"turn": self.current_player().id(),
			"moves_left": list(self.__moves_left__),
			"players": [p.name() for p in self.__players__],
		}