# python-notes
Python miscellany. The modules here serve as examples of how to do everyday things like opening files, getting data from remote sources and returning data. Each script has a corresponding unit test. Many of these tests demonstrate useful techniques for mocking data and dependencies.

## Requirements
Python 3.4+. Python 3.4+ ships with pip and venv (aka virtualenv). 

## Instructions
Activate the virtual environment. Run `. env/Scripts/activate` to activate your virtual environment. Then run `pip install -r requirements.txt` to install the packages required to run the various scripts the python-notes repo.

## Getting Started
Make sure the virtual environment is active. Run `python -m unittest` in the root directory to run all the unit tests.

## Overview

### Concurrency

The [concurrency](https://github.com/b-ritter/python-notes/tree/master/concurrency) module demonstrates how to get the contents of a list of websites in parallel.

### System Ops

[System Ops](https://github.com/b-ritter/python-notes/tree/master/systemops) contains scripts that interact with the environment and/or file system. 

### Years

[Years](https://github.com/b-ritter/python-notes/tree/master/years) simply demonstrates a list comprehension. Its tests show how to handle input errors.

### Database

[Database](https://github.com/b-ritter/python-notes/tree/master/database) explores the sqlalchemy library for database abstraction.