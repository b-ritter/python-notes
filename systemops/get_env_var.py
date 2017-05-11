""" Provide access to environment variables """
import os

def host():
    """ Return the ip address and port of the localhost """
    try:
        hostname = os.environ.get('local')
        if hostname is None:
            raise OSError
    except OSError:
        raise
    else:
        return hostname

if __name__ == "__main__":
    print(host())
