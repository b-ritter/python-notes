
def years(start, end):
    """ Build a list of years as strings."""
    end = end + 1
    return [str(yr) for yr in range(start, end)]

if __name__ == '__main__':
    print(years(2006, 2015))
