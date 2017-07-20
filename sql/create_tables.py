"""
From https://en.wikipedia.org/wiki/Join_(SQL)
"""

import sqlite3

conn = sqlite3.connect('org.db')

c = conn.cursor()

with open('setup.sql') as s:
    create = s.read()

c.executescript(create)

with open('query.sql') as q:
    select = q.read()

results = c.execute(select)

print(results.fetchall())