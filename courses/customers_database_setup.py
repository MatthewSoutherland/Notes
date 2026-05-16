import sqlite3


conn = sqlite3.connect("customers.db")

c = conn.cursor()

c.execute(
    """CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
)

c.execute(
    "INSERT INTO customers(username, email, password) VALUES('matt', 'mgsoutherland529@gmail.com', 'matt')"
)

c.execute(
    "INSERT INTO customers(username, email, password) VALUES('guy', 'mgsoutherland529@gmail.com', 'guy')"
)

c.execute(
    "INSERT INTO customers(username, email, password) VALUES('admin', 'mgsoutherland529@gmail.com', 'admin')"
)

conn.commit()

conn.close()
