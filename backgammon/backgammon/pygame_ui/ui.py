import sys
import pygame
from pygame import Rect

from backgammon.core.game import BackgammonGame

WIDTH, HEIGHT = 900, 600
BG = (33, 36, 46)
POINT_LIGHT = (214, 162, 99)
POINT_DARK = (143, 97, 60)
WHITE = (240, 240, 240)
RED = (200, 64, 64)


def draw_board(screen: pygame.Surface, game: BackgammonGame) -> None:
	board = game.board()
	points = board.points()
	screen.fill(BG)
	triangle_width = WIDTH // 12
	triangle_height = HEIGHT // 2
	font = pygame.font.SysFont(None, 24)
	# Top row points 12..23
	for i in range(12):
		x = i * triangle_width
		color = POINT_LIGHT if i % 2 == 0 else POINT_DARK
		pygame.draw.polygon(
			screen,
			color,
			[(x, 0), (x + triangle_width, 0), (x + triangle_width // 2, triangle_height)],
		)
		count = points[12 + i]
		label = font.render(str(abs(count)) if count != 0 else "", True, WHITE)
		screen.blit(label, (x + triangle_width // 2 - 8, triangle_height // 2 - 12))
	# Bottom row points 11..0
	for i in range(12):
		x = i * triangle_width
		color = POINT_LIGHT if i % 2 == 1 else POINT_DARK
		pygame.draw.polygon(
			screen,
			color,
			[(x, HEIGHT), (x + triangle_width, HEIGHT), (x + triangle_width // 2, HEIGHT - triangle_height)],
		)
		count = points[11 - i]
		label = font.render(str(abs(count)) if count != 0 else "", True, WHITE)
		screen.blit(label, (x + triangle_width // 2 - 8, HEIGHT - triangle_height // 2 - 12))

	# Text info
	info = font.render(
		f"Turno: {game.current_player().name()} Dados: {game.moves_left()}", True, WHITE
	)
	screen.blit(info, (10, HEIGHT // 2 - 12))


def main() -> None:
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Backgammon - Pygame UI")
	clock = pygame.time.Clock()
	game = BackgammonGame()
	game.roll()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game.roll()
				elif event.key == pygame.K_RETURN:
					game.end_turn()

		draw_board(screen, game)
		pygame.display.flip()
		clock.tick(30)

	pygame.quit()


if __name__ == "__main__":
	main()