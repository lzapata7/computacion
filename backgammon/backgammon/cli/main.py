import sys
import click

from backgammon.core.game import BackgammonGame


@click.group()
def cli() -> None:
	"""Backgammon CLI."""


@cli.command()
@click.option("--p1", default="Blancas", help="Nombre del jugador 1")
@click.option("--p2", default="Negras", help="Nombre del jugador 2")
def play(p1: str, p2: str) -> None:
	"""Jugar una partida en consola (simplificado)."""
	game = BackgammonGame(p1, p2)
	click.echo("Nueva partida de Backgammon")
	while True:
		if not game.moves_left():
			roll = game.roll()
			click.echo(f"Turno de {game.current_player().name()} - Tirada: {roll} -> {game.moves_left()}")
		if game.winner() is not None:
			break
		moves = game.moves_left()
		if not moves:
			game.end_turn()
			continue
		try:
			cmd = click.prompt("Movimiento (from_idx o BAR, die) o 'end'", type=str)
			if cmd.strip().lower() == "end":
				game.end_turn()
				continue
			src_s, die_s = [p.strip() for p in cmd.split(",")]
			from_idx = None if src_s.lower() == "bar" else int(src_s)
			die = int(die_s)
			ok = game.move(from_idx, die)
			if not ok:
				click.echo("Movimiento inválido")
			else:
				click.echo(f"Hecho. Restan: {game.moves_left()}")
			if not game.moves_left():
				game.end_turn()
		except Exception as exc:  # noqa: BLE001
			click.echo(f"Error: {exc}")

	winner = game.winner()
	click.echo(f"Ganador: {'P1' if winner == 1 else 'P2'}")


if __name__ == "__main__":
	cli()