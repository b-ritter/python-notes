""" Open a json file and read the data"""
import json

def get_stooges(stooge_file):
    """Get regular and psychedelic stooges."""
    with open(stooge_file) as data:
        stooges = json.load(data)
    return stooges

if __name__ == "__main__":
    STOOGES = get_stooges('data/stooges.json')
    print(STOOGES)
