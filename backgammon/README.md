# Backgammon (Python)

Proyecto de Backgammon con lógica separada del UI, jugable por CLI y Pygame.

## Estructura

/backgammon/
- core: lógica del juego (independiente de UI)
- cli: interfaz de línea de comando
- pygame_ui: interfaz gráfica con Pygame
- assets: imágenes/sonidos

## Requisitos
- Python 3.10+

Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar CLI
```bash
python -m backgammon.cli.main
```

## Ejecutar UI Pygame
```bash
python -m backgammon.pygame_ui.ui
```

## Tests y Cobertura
```bash
pytest
```
La cobertura se reporta con `--cov` (ver `pytest.ini`).

## Docker (testing y juego)
Construir imagen:
```bash
docker build -t backgammon:dev .
```
Tests:
```bash
docker run --rm backgammon:dev pytest
```
CLI:
```bash
docker run -it --rm backgammon:dev python -m backgammon.cli.main
```
Pygame (requiere entorno gráfico):
```bash
docker run -it --rm --env SDL_VIDEODRIVER=dummy backgammon:dev python -m backgammon.pygame_ui.ui
```

## Licencia
MIT