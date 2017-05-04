
def years(start, end):
    """ Build a list of years in the recent past/future as strings."""
    end = end + 1
    try:
        too_far_in_past = start >= 2000
        too_far_in_future = end <= 2020
        if too_far_in_future or too_far_in_past:
            raise ValueError
    except ValueError as e:
        print(e)
        raise
    else:
        return [str(yr) for yr in range(start, end)]

if __name__ == '__main__':
    print(years(2006, 2015))
