__author__ = 'sivins'

import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE expenses")
    c.execute("CREATE TABLE expenses(date TEXT, amount TEXT, description TEXT, category TEXT)")
    c.execute('INSERT INTO expenses VALUES("12/24/13", "23.13", "McDonalds", "Fast Food")')