import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY,"
                     "user_name TEXT,"
                     "user_phone TEXT,"
                     "telegram_id TEXT);"
                     "CREATE TABLE IF NOT EXISTS art_glazing("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS glazing_24("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS glazing_32("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS glazing_40("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS art_jalousie("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS jalousie_h16("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS jalousie_h25("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS jalousie_hor_fix("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS jalousie_v127("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS jalousie_v89("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS jalousie_vert_fix("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS art_mosquito_inside("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS art_mosquito_outside("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS mosquito_inside_white("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS mosquito_inside_brown("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS mosquito_inside_anthracite("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS mosquito_outside_white("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS mosquito_outside_brown("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS art_reflux("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS reflux_price("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS art_windowsill("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "call_data TEXT);"
                     "CREATE TABLE IF NOT EXISTS windowsill_white("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS windowsill_plug_white("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS windowsill_gold("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS windowsill_plug_gold("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);"
                     "CREATE TABLE IF NOT EXISTS profit_work_waste("
                     "id INTEGER PRIMARY KEY,"
                     "art TEXT,"
                     "price REAL);")
            self.cursor.executescript(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print("Помилка під час створення: ", Error)

    def add_user(self, user_name, user_phone, telegram_id):
        self.cursor.execute(f"INSERT INTO users (user_name, user_phone, telegram_id, discount) VALUES (?, ?, ?, ?)",
                            (user_name, user_phone, telegram_id, int(5)))
        self.connection.commit()

    def select_user_id(self, telegram_id):
        users = self.cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()

    def db_select_all(self, table_name):
        result = self.cursor.execute("SELECT * FROM {}".format(table_name))
        return result.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
