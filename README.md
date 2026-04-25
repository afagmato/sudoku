# Sudoku

> Generador i joc de Sudoku per terminal amb tres nivells de dificultat.

---

## Funcionalitats

- Generació aleatòria d'un sudoku vàlid en cada partida
- Tres nivells de dificultat: fàcil, mitjà i difícil
- Validació de moviments en temps real
- Detecció automàtica de victòria

## Tecnologies

- Python 3.x
- Sense dependències externes

## Com executar-lo

1. Clona el repositori:
   ```bash
   git clone https://github.com/afagmato/sudoku.git
   cd sudoku
   ```

2. Executa el joc:
   ```bash
   python main.py
   ```

3. Tria el nivell i introdueix fila, columna i número per jugar.

## Com funciona

El taulell es genera amb un algorisme de **backtracking recursiu**: omple la graella 9x9 provant números aleatoris i enretirant-se quan troba un conflicte. Un cop generat, s'amaguen caselles segons el nivell triat.

## Estructura

```
sudoku/
├── main.py
└── README.md
```

## Autor

**afagmato**
- GitHub: [@afagmato](https://github.com/afagmato)
