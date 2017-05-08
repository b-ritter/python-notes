import json

def get_stooges(stooge_file):
    """Get regular and psychedelic stooges."""
    with open(stooge_file) as f:
        stooges = json.load(f)

    print(stooges)

if __name__ == '__main__':
    get_stooges('stooges.json')
