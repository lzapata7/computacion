import random
from typing import List, Tuple


class Dice:
	"""Lógica de tiradas de dados.

	Atributos:
	- __last_roll__: última tirada (tupla de dos enteros)
	"""

	def __init__(self) -> None:
		self.__last_roll__: Tuple[int, int] | None = None

	def roll(self) -> Tuple[int, int]:
		"""Tira dos dados de seis caras.

		Returns: (d1, d2)
		"""
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		self.__last_roll__ = (d1, d2)
		return self.__last_roll__

	def moves_from_roll(self, roll: Tuple[int, int] | None = None) -> List[int]:
		"""Convierte la tirada en una lista de movimientos disponibles.

		Si es doble, devuelve cuatro movimientos iguales.
		"""
		if roll is None:
			roll = self.__last_roll__
		if roll is None:
			raise ValueError("No hay tirada disponible")
		d1, d2 = roll
		if d1 == d2:
			return [d1, d1, d1, d1]
		return [d1, d2]