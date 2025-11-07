from dataclasses import dataclass
import datatypes.timestamp as ts

@dataclass
class Date:
    year: int
    month: int
    day: int
    timestamp: ts.TimeStamp

def make_date(year: int, month: int, day: int, time: ts.TimeStamp = ts.TimeStamp(0,0,0)) -> Date:
    """ Creates an instance of Date, coresponding to the given date, if time is omitted set to midnight."""
    return Date(year, month, day, time)

def _is_leap_year(y: int) -> bool:
    """ Checks if the given year is a leap year."""
    return (y % 400 == 0 or
            (y % 4 == 0 and 
            y % 100 != 0))

def _days_in_month(m: int, y: int) -> int:
    """ Returns the number of days in the given month."""
    if m == (4 or 6 or 9 or 11):
        return 30
    elif m == 2:
        if _is_leap_year(y):
            return 29
        else:
            return 28
    else:
        return 31

def valid(year: int, month: int, day: int) -> bool:
    """ Checks if the given arguments is a valid date."""
    return (1 <= month <= 12 and
            1 <= day <= _days_in_month(day, year)) #but how to correct for a valid year?

def skip_day(d: Date) -> None:
    """ Adds one day to d."""
    d.day = d.day + 1
    if d.day == _days_in_month(d.month, d.year) + 1:
        d.day = 1
        skip_month(d)

def skip_month(d: Date) -> None:
    """ Adds one month to d."""
    d.month = d.month + 1
    if d.month == 13:
        d.month = 1
        skip_year(d)

def skip_year(d: Date) -> None:
    """ Adds one year to d."""
    d.year = d.year + 1

def skip_time(d: Date, t: ts.TimeStamp) -> None:
    """ Skips d forward by the indicated amount of time t."""
    if (d.timestamp.hours + t.hours > 23 or
        (d.timestamp.hours + t.hours == 23 and
         d.timestamp.minutes + t.minutes + (d.timestamp.seconds + t.seconds) // 60) > 59):
        skip_day(d)
    ts.skip(d.timestamp, t)

def equals(d1: Date, d2: Date) -> bool:
    """ Determines wether d1 and d2 represents the same date."""
    return (d1.year == d2.year and
            d1.month == d2.month and
            d1.day == d2.day and
            ts.equals(d1.timestamp, d2.timestamp))

def copy(d: Date) -> Date:
    """ Returns a copy of d."""
    return Date(d.year, d.month, d.day, d.timestamp)

def to_string(d: Date) -> str:
    """ Returns a textual representation of d."""
    output = str(d.year) + '-'
    if d.month < 10:
        output = output + '0'
    output = output + str(d.month) + '-'
    if d.day < 10:
        output = output + '0'
    output = output + str(d.day) + '(' + ts.to_string(d.timestamp) + ')'
    return output