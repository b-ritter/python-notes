""" Demonstrates partitioning arrays """

def list_diff(list_a, list_b):
    """ Expects two lists. Returns an array of the items in a that aren't in b. """
    return [item for item in list_a if item not in list_b]

if __name__ == "__main__":
    A = [
        ('Las Vegas', 'Nevada'),
        ('Los Angeles', 'California'),
        ('Brooklyn', 'New York'),
        ('Dallas', 'Texas'),
        ('Costa Mesa', 'California')
        ]
    B = [
        ('Las Vegas', 'Nevada'),
        ('Brooklyn', 'New York'),
        ('Santa Barbara', 'California')
        ]
    print(list_diff(A, B))
