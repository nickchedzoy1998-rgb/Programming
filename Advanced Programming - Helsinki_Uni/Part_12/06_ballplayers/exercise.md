# BallPlayers

The exercise template defines a `BallPlayer` class with these public
attributes:

- `name`
- `number` (shirt number)
- `goals` (scored goals)
- `assists` (completed assists)
- `minutes` (minutes played)

Implement the following functions. Each function returns a different kind of
value.

## Most goals

Write a function named `most_goals(players: list)` that returns the name of the
player who scored the most goals.

```python
def most_goals(players: list) -> str:
    """Return the name of the player with the most goals."""
    ...
```

## Most points

Write a function named `most_points(players: list)` that returns a tuple with the
name and shirt number of the player who scored the most points. Points are
calculated as `goals + assists`.

```python
def most_points(players: list) -> tuple:
    """Return (name, number) of the player with the most points."""
    ...
```

## Least minutes

Write a function named `least_minutes(players: list)` that returns the
`BallPlayer` object with the fewest minutes played.

```python
def least_minutes(players: list):
    """Return the BallPlayer who played the fewest minutes."""
    ...
```

## Example

Test your functions with:

```python
if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)

    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))
```

Sample output:

```text
Archie Bonkers
('Cruella De Hill', 9)
BallPlayer(name=Donald Quack, number=4, goals=3, passes=9, minutes=12)
```
