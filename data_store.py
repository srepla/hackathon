import sqlite3


class DataStore:

    def __init__(self):

        try:
            self._conn = sqlite3.connect('../res/sensors.db')
            cur = self._conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS temp_sensor(temp_c, humidity);''')
            self._conn.commit()
        except Exception as e:
            print(e)
            self._conn.close()

    def store_in_db(self, temp_c, humidity):
        cur = self._conn.cursor()
        cur.execute('''INSERT INTO temp_sensor(temp_c, humidity) VALUES (?, ?);''', (temp_c, humidity))
        self._conn.commit()

    def load_from_db(self):
        cur = self._conn.cursor()
        cur.execute('''SELECT * FROM temp_sensor;''')
        return cur.fetchone()
