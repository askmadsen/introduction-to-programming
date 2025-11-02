from dataclasses import dataclass

@dataclass
class Point2D:
    x: float
    y: float


def make_point(x: float, y: float) -> Point2D:
    """ Returns a new instance of Point2D with the given coordinates."""
    return Point2D(x,y)


def move(p: Point2D, dx: float, dy: float) -> None:
    """ Moves p according to the vector (dx,dy)."""
    p.x = p.x + dx
    p.y = p.y + dy


def distance_to_origin(p: Point2D) -> float:
    """ Returns p's distande to the origin."""
    return (p.x ** 2 + p.y ** 2) ** 0.5

def distance(p1: Point2D, p2: Point2D) -> float:
    """ Returns the distance between p1 and p2."""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return (dx * dx + dy * dy) ** 0.5

def equals(p1: Point2D, p2: Point2D) -> bool:
    """ Determines wether p1 and p2 represents the same point."""
    return (p1.x == p2.x and
            p1.y == p2.y)


def copy(p: Point2D) -> Point2D:
    """ Returns a copy of p."""
    return Point2D(p.x, p.y)


def to_string(p: Point2D) -> str:
    """ Returns a textual representation of p."""
    return '(' + str(p.x) + ',' + ' ' + str(p.y) + ')'