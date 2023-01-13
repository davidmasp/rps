## db stuff
import sqlite3
import datetime

class Users:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id text, name text, date text, lastdate text, wins int, loses int, draws int)''')
        self.conn.commit()

    def insert(self, id, name):
        test = self.select(id)
        if test is not None:
            return 
        today = datetime.date.today()
        date_str = today.strftime("%Y-%m-%d")
        win_base = 0
        lose_base = 0
        streak_base = 0
        draw_base = 0
        self.c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", (id, name, date_str, date_str, win_base, lose_base, draw_base))
        self.conn.commit()

    def select(self, id):
        self.c.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.c.fetchone()

    def update(self, id, result):
        today = datetime.date.today()
        date_str = today.strftime("%Y-%m-%d")
        status = self.select(id)
        if result == "win":
            new_record = status[4] + 1
            record_type = "wins"
        elif result == "lose":
            new_record = status[5] + 1
            record_type = "loses"
        elif result == "draw":
            new_record = status[6] + 1
            record_type = "draws"
        else: 
            raise ValueError("Error: Invalid result")
        query = "UPDATE users SET {} = ?, lastdate = ? WHERE id = ?".format(record_type)
        self.c.execute(query, (new_record, date_str, id))
        self.conn.commit()

    def delete(self, id):
        self.c.execute("DELETE FROM users WHERE id = ?", (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


