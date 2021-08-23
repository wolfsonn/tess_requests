import sqlite3
import pandas as pd

import tess_requests
from process_requests import process


# def create_db():
#     conn = sqlite3.connect('request.db')
#     c = conn.cursor()
#     c.execute("""   CREATE TABLE requests (
#                     r_action text,
#                     r_case text,
#                     r_egn text,
#                     r_status text
#                 )""")
#     conn.commit()
#     conn.close()


def add_requests(folder):
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.executemany("INSERT INTO requests VALUES (?, ?, ?, 'pending')", process(folder))
    conn.commit()
    conn.close()


def export_csv_act_status(act, status):
    conn = sqlite3.connect('request.db')
    if (act in tess_requests.Request.ACTIONS.keys() or act == 'none') and (status == 'pending' or status == 'done' or status == 'none'):

        # export all actions, all statuses
        if not act and not status:
            export = pd.read_sql_query("""SELECT * FROM requests""", conn)
            export.to_csv('export_all.csv', index=True)
        # export all actions, status
        elif not act and status:
            export = pd.read_sql_query("""SELECT * FROM requests
                                            WHERE r_status = '{}'""".format(status), conn)
            export.to_csv(f'export_all_{status}.csv', index=True)
        # export action, all statuses
        elif act and not status:
            export = pd.read_sql_query("""SELECT * FROM requests
                                            WHERE r_action = '{}'""".format(act), conn)
            export.to_csv(f'export_{act}.csv', index=True)
        # export action, status
        elif act and status:
            export = pd.read_sql_query("""SELECT * FROM requests
                                            WHERE r_action = '{}' AND r_status = '{}'""".format(act, status), conn)
            export.to_csv(f'{act}_{status}.csv', index=True)
    conn.commit()
    conn.close()


def export_taxes(act, status):
    conn = sqlite3.connect('request.db')
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    # export taxes for all actions, all statuses
    if not act and not status:
        export = c.execute("""SELECT r_case FROM requests""").fetchall()
    # export taxes for all actions, status
    elif not act and status:
        export = c.execute("""SELECT r_case FROM requests
                            WHERE r_status = '{}'""".format(status)).fetchall()
    # export taxes for action, all statuses
    elif act and not status:
        export = c.execute("""SELECT r_case FROM requests
                            WHERE r_action = '{}'""".format(act)).fetchall()
    # export taxes for action, status
    elif act and status:
        export = c.execute("""SELECT r_case FROM requests
                            WHERE r_action = '{}' AND r_status = '{}'""".format(act, status)).fetchall()
    conn.commit()
    conn.close()
    return export


def set_status(act, status, new_status):
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    # set status all actions, all statuses
    if not act and not status:
        c.execute("""UPDATE requests SET r_status = '{}'""".format(new_status)).fetchall()
    # export all actions, status
    elif not act and status:
        c.execute("""UPDATE requests SET r_status = '{}'
                            WHERE r_status = '{}'""".format(new_status, status)).fetchall()
    # export action, all statuses
    elif act and not status:
        c.execute("""UPDATE requests SET r_status = '{}}'
                            WHERE r_action = '{}'""".format(new_status, act)).fetchall()
    # export action, status
    elif act and status:
        c.execute("""UPDATE requests SET r_status = '{}'
                            WHERE r_action = '{}' AND r_status = '{}'""".format(new_status, act, status)).fetchall()
    c.execute("""UPDATE requests SET r_action = 'done'
                WHERE r_status = 'pending'""")
    conn.commit()
    conn.close()


def clear_table():
    conn = sqlite3.connect('request.db')
    c = conn.cursor()
    c.execute("DELETE FROM requests")
    conn.commit()
    conn.close()

# clear_table()