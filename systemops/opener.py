import json


def get_stooges(stooge_file):
    """Get regular and psychedelic stooges."""
    with open(stooge_file) as data:
        stooges = json.load(data)
    return stooges

if __name__ == '__main__':
    print(get_stooges('stooges.json'))
