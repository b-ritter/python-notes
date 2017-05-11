import os

def host():
    try:
        hostname = os.environ.get('local')
        if hostname == None:
            raise OSError
    except OSError as err:
        raise
    else:
        return hostname

if __name__ == "__main__":
    print(host())