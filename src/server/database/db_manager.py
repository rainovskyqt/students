import sqlite3
import os

# from ..settings import DB_PATH

from settings import DB_PATH

class DBManager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        print(db_path, self.db_path)

    def check_base(self):
        return os.path.exists(self.db_path)

    def connect_to_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur

    def create_base(self, script_path: str):
        conn, cur = self.connect_to_base()
        try:
            cur.executescript(open(script_path).read())
            conn.commit()
            conn.close()
        except Exception as ex:
            print(ex)
            os.remove(self.db_path)

    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_to_base()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            return {"code": 200, "data": result}
        except sqlite3.Error as er:
            print(str(er))
            return {"code": 500}
        finally:
            conn.close()


base_manager = DBManager(DB_PATH)