from __future__ import annotations
from typing import Dict, List, Optional


class Board:
	"""Representa el tablero de Backgammon (24 puntos, barra y salida).

	Internamente se representa cada punto como un entero:
	- > 0: cantidad de fichas del jugador 1
	- < 0: cantidad de fichas del jugador -1

	Atributos:
	- __points__: lista de 24 enteros representando las pilas por punto
	- __bar__: fichas capturadas por jugador {1: int, -1: int}
	- __born_off__: fichas fuera del tablero (bear-off) {1: int, -1: int}
	"""

	NUM_POINTS = 24

	def __init__(self) -> None:
		self.__points__: List[int] = [0 for _ in range(self.NUM_POINTS)]
		self.__bar__: Dict[int, int] = {1: 0, -1: 0}
		self.__born_off__: Dict[int, int] = {1: 0, -1: 0}
		self._setup_standard()

	def _setup_standard(self) -> None:
		# Setup estándar
		self.__points__ = [0 for _ in range(self.NUM_POINTS)]
		self.__points__[23] = 2  # P1
		self.__points__[12] = 5  # P1
		self.__points__[7] = 3   # P1
		self.__points__[5] = 5   # P1
		self.__points__[0] = -2  # P2
		self.__points__[11] = -5 # P2
		self.__points__[16] = -3 # P2
		self.__points__[18] = -5 # P2
		self.__bar__ = {1: 0, -1: 0}
		self.__born_off__ = {1: 0, -1: 0}

	def copy(self) -> Board:
		b = Board()
		b.__points__ = self.__points__[:]
		b.__bar__ = dict(self.__bar__)
		b.__born_off__ = dict(self.__born_off__)
		return b

	def points(self) -> List[int]:
		return self.__points__

	def bar(self, player: int) -> int:
		return self.__bar__[player]

	def born_off(self, player: int) -> int:
		return self.__born_off__[player]

	def is_point_open(self, player: int, index: int) -> bool:
		val = self.__points__[index]
		if player == 1:
			return val >= -1
		else:
			return val <= 1

	def has_all_in_home(self, player: int) -> bool:
		if player == 1:
			start, end = 18, 23
			# No debe haber fichas fuera de casa ni en barra
			if self.__bar__[1] > 0:
				return False
			for idx, val in enumerate(self.__points__):
				if idx < start and val > 0:
					return False
			return True
		else:
			start, end = 0, 5
			if self.__bar__[-1] > 0:
				return False
			for idx, val in enumerate(self.__points__):
				if idx > 5 and val < 0:
					return False
			return True

	def _entry_index_from_bar(self, player: int, die: int) -> int:
		if player == 1:
			return die - 1  # entra por [0..5]
		else:
			return 24 - die  # entra por [23..18]

	def can_enter_from_bar(self, player: int, die: int) -> bool:
		idx = self._entry_index_from_bar(player, die)
		return self.is_point_open(player, idx)

	def _apply_hit_if_needed(self, player: int, dest: int) -> None:
		val = self.__points__[dest]
		if player == 1 and val == -1:
			self.__points__[dest] = 0
			self.__bar__[-1] += 1
		elif player == -1 and val == 1:
			self.__points__[dest] = 0
			self.__bar__[1] += 1

	def move_from_bar(self, player: int, die: int) -> bool:
		"""Intenta ingresar una ficha desde la barra usando `die`.
		Devuelve True si se realizó el movimiento.
		"""
		if self.__bar__[player] <= 0:
			return False
		idx = self._entry_index_from_bar(player, die)
		if not self.is_point_open(player, idx):
			return False
		self._apply_hit_if_needed(player, idx)
		if player == 1:
			self.__points__[idx] += 1
		else:
			self.__points__[idx] -= 1
		self.__bar__[player] -= 1
		return True

	def _is_bearing_off_move(self, player: int, from_idx: int, die: int) -> bool:
		if player == 1:
			return from_idx + die >= 24
		else:
			return from_idx - die < 0

	def _has_checkers_beyond(self, player: int, from_idx: int) -> bool:
		if player == 1:
			# fichas en índices mayores a from_idx dentro de casa
			for i in range(from_idx + 1, 24):
				if self.__points__[i] > 0:
					return True
			return False
		else:
			for i in range(0, from_idx):
				if self.__points__[i] < 0:
					return True
			return False

	def apply_move(self, player: int, from_idx: Optional[int], die: int) -> bool:
		"""Aplica un movimiento si es legal.

		- Si `from_idx` es None, intenta entrar desde la barra.
		- Maneja capturas y bearing off.
		Devuelve True si se realizó el movimiento.
		"""
		# Debe entrar desde la barra si tiene fichas allí
		if self.__bar__[player] > 0:
			if from_idx is not None:
				return False
			return self.move_from_bar(player, die)

		if from_idx is None:
			return False

		val = self.__points__[from_idx]
		if player == 1 and val <= 0:
			return False
		if player == -1 and val >= 0:
			return False

		# Destino
		if player == 1:
			dest = from_idx + die
		else:
			dest = from_idx - die

		# Bearing off
		if self._is_bearing_off_move(player, from_idx, die):
			if not self.has_all_in_home(player):
				return False
			# Regla exacta o mayor si no hay más allá
			if player == 1:
				distance = 24 - from_idx
				if die == distance or not self._has_checkers_beyond(1, from_idx):
					self.__points__[from_idx] -= 1
					self.__born_off__[1] += 1
					return True
			else:
				distance = from_idx + 1
				if die == distance or not self._has_checkers_beyond(-1, from_idx):
					self.__points__[from_idx] += 1
					self.__born_off__[-1] += 1
					return True
			return False

		# Movimiento normal dentro del tablero
		if dest < 0 or dest >= 24:
			return False
		if not self.is_point_open(player, dest):
			return False
		self._apply_hit_if_needed(player, dest)
		if player == 1:
			self.__points__[from_idx] -= 1
			self.__points__[dest] += 1
		else:
			self.__points__[from_idx] += 1
			self.__points__[dest] -= 1
		return True

	def winner(self) -> Optional[int]:
		if self.__born_off__[1] >= 15:
			return 1
		if self.__born_off__[-1] >= 15:
			return -1
		return None