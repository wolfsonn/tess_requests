import sqlite3
from process_requests import process


def create_db():
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("""   CREATE TABLE requests (
                    r_action text,
                    r_case text,
                    r_egn text,
                    r_status text
                )""")
    conn.commit()
    conn.close()


def add_requests():
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.executemany("INSERT INTO requests VALUES (?, ?, ?, 'pending')", process())
    conn.commit()
    conn.close()


def export_all():
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("SELECT * FROM requests")
    export = c.fetchall()
    conn.commit()
    conn.close()


def export_one(action):
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("SELECT * FROM requests WHERE r_action = (?)", action)
    export = c.fetchall()
    conn.commit()
    conn.close()


def mark_done_all():
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("UPDATE * FROM requests SET r_action = 'done'")
    conn.commit()
    conn.close()


def mark_done_one():
    action = input('choose action: ')
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("UPDATE requests SET r_status = 'done' WHERE r_action = (?)", (action,))
    conn.commit()
    conn.close()


mark_done_one()
