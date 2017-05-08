
def years(start, end):
    """ Build a list of years in the recent past/future as strings."""

    try:
        too_far_in_past = start <= 1999
        too_far_in_future = end >= 2020
        if too_far_in_future or too_far_in_past:
            raise ValueError
    except ValueError:
        raise
    else:
        end = end + 1
        return [str(yr) for yr in range(start, end)]

if __name__ == '__main__':
    print(years(2000, 2015))
