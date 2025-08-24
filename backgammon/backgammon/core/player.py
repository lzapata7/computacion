class Player:
	"""Representa a un jugador.

	Atributos:
	- __name__: nombre del jugador
	- __id__: 1 (jugador uno) o -1 (jugador dos)
	- __direction__: +1 si avanza hacia índices mayores, -1 hacia menores
	- __home_range__: tupla (inicio, fin) inclusive del tablero propio de casa
	"""

	def __init__(self, name: str, player_id: int) -> None:
		self.__name__ = name
		self.__id__ = player_id
		self.__direction__ = 1 if player_id == 1 else -1
		# Rango de casa: P1 [18..23], P2 [0..5]
		self.__home_range__ = (18, 23) if player_id == 1 else (0, 5)

	def id(self) -> int:
		return self.__id__

	def name(self) -> str:
		return self.__name__

	def direction(self) -> int:
		return self.__direction__

	def home_range(self) -> tuple[int, int]:
		return self.__home_range__