import sqlite3


class DataStore:

    def __init__(self):

        try:
            self._conn = sqlite3.connect('res/sensors.db', check_same_thread=False)
            cur = self._conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS temp_sensor(
            id INTEGER PRIMARY KEY NOT NULL, 
            temp_c NOT NULL,
            humidity NOT NULL
            );''')
            self._conn.commit()
        except Exception as e:
            print(e)
            self._conn.close()

    def store_in_db(self, temp_c, humidity):
        cur = self._conn.cursor()
        cur.execute('''REPLACE INTO temp_sensor(id, temp_c, humidity) VALUES (1, ?, ?);''', (temp_c, humidity))
        self._conn.commit()

    def load_from_db(self):
        cur = self._conn.cursor()
        cur.execute('''SELECT temp_c, humidity FROM temp_sensor WHERE id = 1;''')
        return cur.fetchone()