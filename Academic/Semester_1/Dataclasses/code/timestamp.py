from dataclasses import dataclass

@dataclass
class TimeStamp:
    hours: int
    minutes: int
    seconds: int

def make_timestamp(h: int = 0, m: int = 0, s: int = 0) -> TimeStamp:
    """ Returns an instance of TimeStamp representing the given time,
        which should be valid. Absent arguments defaults to 0."""
    return TimeStamp(h,m,s)

def valid(h: int, m: int, s: int) -> bool:
    """ Checks wether the given arguments is in a valid range.
    """
    return (0 <= h <= 24 and
            0 <= m < 60 and
            0 <= s < 60)

def get_seconds(t: TimeStamp) -> int:
    """ Returns the number of seconds represented by the timestamp t."""
    return t.seconds

def get_minutes(t: TimeStamp) -> int:
    """ Returns the number of minutes represented by the timestamp t."""
    return t.minutes

def get_hours(t: TimeStamp) -> int:
    """ Returns the number of hours represented by the timestamp t."""
    return t.hours

def skip_second(t: TimeStamp) -> None:
    """ Adds one second to t."""
    t.seconds = t.seconds + 1
    if t.seconds == 60:
        t.seconds = 0
        skip_minute(t)

def skip_minute(t: TimeStamp) -> None:
    """ Adds one minute to t."""
    t.minutes = t.minutes + 1
    if t.minutes == 60:
        t.minutes = 0
        skip_hour(t)

def skip_hour(t: TimeStamp) -> None:
    """ Adds one hour to t."""
    t.hours = t.hours + 1
    if t.hours == 24:
        t.hours = 0

def fix_overflow(t: TimeStamp) -> None:
    """ Fixes the overflow of the timestamp t."""
    t.minutes = t.minutes + t.seconds // 60
    t.hours = t.hours + t.minutes // 60

    t.seconds = t.seconds % 60
    t.minutes = t.minutes % 60
    t.hours = t.hours % 24

def skip(t1: TimeStamp, t2: TimeStamp) -> None:
    """ Adds the amount of time described in t2 to t1."""
    t1.seconds = t1.seconds + t2.seconds
    t1.minutes = t1.minutes + t2.minutes
    t1.hours = t1.hours + t2.hours
    fix_overflow(t1)

def equals(t1: TimeStamp, t2: TimeStamp) -> bool:
    """ Checks if t1 and t2 represents the same timestamp."""
    return(t1.seconds == t2.seconds and
           t1.minutes == t2.minutes and
           t1.hours == t2.hours)

def copy(t: TimeStamp) -> TimeStamp:
    """ Returns a copy of the timestamp t."""
    return TimeStamp(t.hours, t.minutes, t.hours)

def to_string(t: TimeStamp) -> str:
    """ Returns a textual representation of t."""
    output = str(t.hours) + ':'
    if t.minutes < 10:
        output = output + '0'
    output = output + str(t.minutes) + ':'
    if t.seconds < 10:
        output = output + '0'
    output = output + str(t.seconds)
    return output

from time import sleep

def iterate_each_second(t: TimeStamp, n: int):
    """ Prints and increments the timestamp every second for n seconds."""
    for i in range(n):
        skip_second(t)
        print(to_string(t))
        sleep(1)