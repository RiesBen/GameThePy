<p align="center">
    <picture align="center">
      <img alt="GameThePy fancy logo" src=".img%2Flogo2_small.png" width=35% >
    </picture>
</p>

GameThePy
===============
 A GameTheory library in it's making


## Example

### Simple games

```python
# Imports 
from gamethepy import Game
from gamethepy import RandomStrategyPlayer
from gamethepy.normal_form_games import PrisonersDilemmaGame

# Build the Game
players = [RandomStrategyPlayer() for _ in range(2)]
rules = PrisonersDilemmaGame()
game = Game(players=players, metric=rules)

# Play
results = game.turns(10)

# Outcome
results
```

#### Result - Output:

|      | PlayerA  | PlayerB  |
|------|----------|----------|
| Turn |          |          |
| 0    | 2        | -1       |
| 1    | 1        | 1        |
| 2    | -2       | -2       |
| 3    | -1       | 2        |
| 4    | 2        | -1       |
| 5    | 1        | 1        |
| 6    | 2        | -1       |
| 7    | -2       | -2       |
| 8    | -2       | -2       |
| 9    | -2       | -2       |