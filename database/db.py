import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("user.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                                num INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id VARCHAR,
                                crypto TEXT,
                                timing INTEGER
                            )""")


    def user_registration(self, message_id):
        tg_id = message_id
        self.cursor.execute(f"SELECT user_id FROM users WHERE user_id = {tg_id}")
        data = self.cursor.fetchone()

        if data is None:
            id = tg_id

            self.cursor.execute("INSERT INTO users(user_id) VALUES(?)", [id])
            self.conn.commit()

    def timing(self, time, message_id):
        self.cursor.execute(f"UPDATE users SET timing = ? WHERE user_id = {message_id}", [time])
        self.conn.commit()

    def get_timing(self, message_id):
        self.cursor.execute(f"SELECT timing FROM users WHERE user_id = {message_id}")
        time = self.cursor.fetchone()
        return time

    def crypto(self, crypto):
        pass



database = Database()