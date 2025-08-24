# JUSTIFICACION

## Resumen del diseño general
Separación estricta entre lógica (`core`) y presentación (`cli`, `pygame_ui`). `BackgammonGame` orquesta `Board`, `Dice` y `Player`.

## Clases y responsabilidades
- Board: reglas de movimiento, capturas, bar y bear-off.
- Dice: tiradas y expansión a movimientos disponibles.
- Player: identidad y parámetros (dirección, home).
- Checker: entidad mínima de ficha.
- BackgammonGame: turnos, jugadas con dados, fin de partida.

## Atributos y decisiones
Todos los atributos siguen el formato __atributo__. Se elige representación de puntos como enteros firmados para eficiencia y simplicidad.

## Decisiones de diseño relevantes
- Core sin dependencias de UI. 
- Reglas encapsuladas en `Board.apply_move`.
- Serialización mínima para posibles persistencias (Redis).

## Excepciones y manejo de errores
Se validan movimientos y estados; se lanzan `ValueError` donde corresponde (e.g., `Dice.moves_from_roll`). La CLI captura excepciones y muestra mensajes.

## Estrategias de testing y cobertura
Pruebas unitarias de `Board`, `Dice`, `Game` buscando >90% de cobertura del core. Casos: entradas desde barra, captura, bloqueos, bearing-off, victoria.

## SOLID
- SRP: cada clase con responsabilidad única.
- OCP: reglas ampliables (p. ej., variantes) extendiendo `Board`.
- LSP: instancias de `Board`/`Dice` sustituibles por mocks.
- ISP: interfaces pequeñas (métodos específicos por clase).
- DIP: `BackgammonGame` depende de abstracciones públicas de `Board`/`Dice`.

## Anexos
Diagramas UML por agregar durante el cursado.