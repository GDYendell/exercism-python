"""Solution to Ellen's Alien Game exercise."""


from typing import Any, List, Tuple


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        self.__class__.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x: int, new_y: int):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, _other: Any) -> bool:
        pass


def new_aliens_collection(alien_start_positions: List[Tuple[int, int]]):
    return list(Alien(x, y) for x, y in alien_start_positions)