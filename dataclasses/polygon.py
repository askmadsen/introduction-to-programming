import code.point2d as p2d

Polygon = list[p2d.Point2D]


def make_polygon(v: list[p2d.Point2D]) -> Polygon:
    """ Creates a polygon from the list of its vertices."""
    return Polygon([p2d.copy(p) for p in v]) #creates a polygon by deep dopying the lists of points
            

def perimeter(p: Polygon) -> float:
    """ Returns the perimeter of p."""
    perimeter = 0
    for i in range(-1, len(p) - 1):
        perimeter = perimeter + p2d.distance(p[i], p[i + 1])
    return perimeter


def nearest(p: Polygon) -> p2d.Point2D:
    """ Returns the vertex of p closest to the origin."""
    nearest = p[0]
    distance = p2d.distance_to_origin(nearest)
    for point in p:
        p_dist = p2d.distance_to_origin(point)
        if p_dist < distance:
            nearest = point
            distance = p_dist
    return nearest

def longest_side(p: Polygon) -> float:
    """ Returns the length of p's longest side."""
    longest = p2d.distance(p[-1], p[0])
    for i in range(len(p) - 1):
        distance = p2d.distance(p[i], p[i + 1])
        if distance > longest:
            longest = distance
    return longest


def move(p: Polygon, dx: float, dy: float) -> None:
    """ Moves p according to the vector (dx, dy)."""
    for point in p:
        p2d.move(point, dx, dy)


def vertices_in_quadrant(p: Polygon, n: int) -> int:
    """ Returns the number of vertices p has in the n-th quadrant."""
    vertices = 0
    match n:
        case 1:
            for point in p:
                if (point.x > 0 and
                    point.y > 0):
                    vertices = vertices + 1
        case 2:
            for point in p:
                if (point.x < 0 and
                    point.y > 0):
                    vertices = vertices + 1
        case 3:
            for point in p:
                if (point.x < 0 and
                    point.y < 0):
                    vertices = vertices + 1
        case 4:
            for point in p:
                if (point.x > 0 and
                    point.y < 0):
                    vertices = vertices + 1
    return vertices



def is_triangle(p: Polygon) -> bool:
    """ Determines wether p is a triangle."""
    return len(p) == 3

def is_rectangle(p: Polygon) -> bool:
    """ Determines wether p is a rectangle."""
    return len(p) == 4

def equals(p1: Polygon, p2: Polygon) -> bool:
    """ Determines wether p1 and p2 rerpesents the same polygon accounting for the order of the points in p."""
    if len(p1) != len(p2):
        return False
    else:
        i = 0
        j = 0
        while not p2d.equals(p1[i], p2[j]):
            if j == len(p2) - 1:
                return False
            j = j + 1
        equal = True
        while i < len(p1) and equal:
            if not p2d.equals(p1[i], p2[j]):
                equal = False
            elif j == len(p2) - 1:
                j = -1
            i = i + 1
            j = j + 1
        return equal
            
        
        
def copy(p: Polygon) -> Polygon:
    """ Returns a copy of p."""
    return Polygon(p.polygon)

def to_string(p: Polygon) -> str:
    """ Returns a textual representation of p."""
    output = '['
    for point in p:
        output = output + p2d.to_string(point) + ',' + ' '
    output = output + p2d.to_string(p[0]) + ']'
    return output