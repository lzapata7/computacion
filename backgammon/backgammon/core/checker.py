class Checker:
	"""Representa una ficha de Backgammon.

	Atributos:
	- __owner__: identificador del jugador (1 o -1)
	- __id__: identificador único opcional de la ficha
	"""

	def __init__(self, owner: int, checker_id: int | None = None) -> None:
		self.__owner__ = owner
		self.__id__ = checker_id

	def owner(self) -> int:
		"""Devuelve el dueño de la ficha (1 o -1)."""
		return self.__owner__