""" Open a yaml file and read the data"""
import yaml

def get_stuff(file):
    with open(file) as data:
        data = yaml.safe_load(data)
    return data

if __name__ == "__main__":
    stuff = get_stuff('data/stuff.yml')
    print(stuff)
