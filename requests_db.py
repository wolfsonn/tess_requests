import sqlite3
import pandas as pd
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


def export_all_pending():
    conn = sqlite3.connect('request.db')
    export = pd.read_sql_query("""SELECT r_action, r_case, r_egn FROM requests
                                WHERE r_status = 'pending'""", conn)
    export.to_csv('all.csv', index=True)
    conn.commit()
    conn.close()


def export_one_pending(act):
    conn = sqlite3.connect('request.db')
    export = pd.read_sql_query("""SELECT r_action, r_case, r_egn FROM requests
                                WHERE r_action = '{}' AND r_status = 'pending'""".format(act), conn)
    export.to_csv(f'{act}.csv', index=True)
    conn.commit()
    conn.close()


def export_one_for_taxes(act):
    conn = sqlite3.connect('request.db')
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    export = c.execute("""SELECT r_case FROM requests
                    WHERE r_action = '{}' AND r_status = 'pending'""".format(act)).fetchall()
    conn.commit()
    conn.close()
    return export


def mark_done_all():
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("""UPDATE requests SET r_action = 'done'
                WHERE r_status = 'pending'""")
    conn.commit()
    conn.close()


def mark_done_one(act):
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("""UPDATE requests SET r_status = 'pending'
                WHERE r_action = '{}' AND r_status = 'pending'""".format(act))
    conn.commit()
    conn.close()
