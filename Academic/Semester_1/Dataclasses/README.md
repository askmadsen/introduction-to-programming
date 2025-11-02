# Dataclasses Projects

This folder contains exercises and small projects exploring the use of **dataclasses** in Python.  
These projects implement abstractions for points, polygons, timestamps and dates, demonstrating object-oriented design with simple data structures.

## Modules Included

### 1. Point2D

Defines a 2D point with `x` and `y` coordinates and provides utility functions.

#### Functions:
- **make_point(x, y)** – Creates a `Point2D` instance.
- **move(p, dx, dy)** – Moves the point by `(dx, dy)`.
- **distance_to_origin(p)** – Returns the Euclidean distance from the origin.
- **distance(p1, p2)** – Returns the distance between two points.
- **equals(p1, p2)** – Checks if two points are equal.
- **copy(p)** – Returns a copy of a point.
- **to_string(p)** – Returns a textual representation of a point.

#### Example:
```python
from code import point2d as p2d

p = p2d.make_point(1, 2)
q = p2d.make_point(4, 6)
print(p2d.distance(p, q))  # Output: 5.0
```


### 2. Polygon

Represents a polygon as a list of Point2D vertices and provides geometric utilities.

#### Functions:
- **make_polygon(v)** – Creates a polygon from a list of vertices.
- **perimeter(p)** – Returns the perimeter of a polygon.
- **nearest(p)** – Returns the vertex closest to the origin.
- **longest_side(p)** – Returns the length of the longest side.
- **move(p, dx, dy)** – Moves all vertices of the polygon by (dx, dy).
- **vertices_in_quadrant(p, n)** – Counts vertices in the n-th quadrant (1–4).
- **is_triangle(p)** – Checks if the polygon has 3 vertices.
- **is_rectangle(p)** – Checks if the polygon has 4 vertices.
- **equals(p1, p2)** – Checks if two polygons are equal (order matters).
- **copy(p)** – Returns a copy of the polygon.
- **to_string(p)** – Returns a textual representation of the polygon.

#### Example

```python
from code import polygon

vertices = [p2d.make_point(0,0), p2d.make_point(1,0), p2d.make_point(0,1)]
poly = polygon.make_polygon(vertices)
print(polygon.perimeter(poly))  # Output: 3.414213562373095
```

### 3. TimeStamp

Represents a time of day with hours, minutes, and seconds.

#### Functions:

- **make_timestamp(h=0, m=0, s=0)** – Creates a `TimeStamp` instance. Defaults to midnight if arguments are omitted.  
- **valid(h, m, s)** – Checks if the time is valid (0 ≤ h ≤ 24, 0 ≤ m < 60, 0 ≤ s < 60).  
- **get_seconds(t), get_minutes(t), get_hours(t)** – Return the respective component of a timestamp.  
- **skip_second(t), skip_minute(t), skip_hour(t)** – Advance the timestamp by one second, minute, or hour.  
- **fix_overflow(t)** – Corrects overflows for seconds, minutes, and hours.  
- **skip(t1, t2)** – Adds `t2` to `t1`, updating `t1` in place.  
- **equals(t1, t2)** – Checks if two timestamps are equal.  
- **copy(t)** – Returns a copy of the timestamp.  
- **to_string(t)** – Returns a string representation (`HH:MM:SS`).  
- **iterate_each_second(t, n)** – Prints and increments the timestamp every second for `n` seconds.

#### Example:

```python
from code import timestamp as ts

t = ts.make_timestamp(23, 59, 50)
ts.iterate_each_second(t, 15)  # Prints next 15 seconds, wrapping over to next hour/day if needed
```

### 4. Date

Represents a calendar date with year, month, day, and a TimeStamp.

#### Functions:

- **make_date(year, month, day, time=TimeStamp(0,0,0))** – Creates a Date instance; defaults to midnight if no timestamp is given.
- **valid(year, month, day)** – Checks if a date is valid.
- **skip_day(d), skip_month(d), skip_year(d)** – Advances the date by a day, month, or year.
- **skip_time(d, t)** – Advances the date by the specified timestamp t.
- **equals(d1, d2)** – Checks if two dates are identical.
- **copy(d)** – Returns a copy of a date.
- **to_string(d)** – Returns a string representation in YYYY-MM-DD(HH:MM:SS) format.


#### Example:

```python
from code import date
from code import timestamp as ts

d = date.make_date(2025, 11, 2)
print(date.to_string(d))  # Output: "2025-11-02(00:00:00)"

ts.skip_second(d.timestamp)
print(date.to_string(d))  # Output: "2025-11-02(00:00:01)"
```

## Key Learnings

- Used dataclasses for clear and concise data structures.
- Implemented deep copies and equality checks for custom objects.
- Practiced geometric computations with points and polygons.
- Explored date arithmetic and validation, integrating time management.
- Reinforced modularity and reusability in Python projects.