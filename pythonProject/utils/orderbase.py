import sqlite3


class Orderbase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS ПІДВІКОННЯ("
                     "id INTEGER PRIMARY KEY,"
                     "Телефон TEXT,"
                     "Імя TEXT,"
                     "Підвіконня TEXT,"
                     "Колір TEXT,"
                     "Заглушка TEXT,"
                     "Кількість INTEGER,"
                     "Довжина INTEGER,"
                     "В_роботі INTEGER,"
                     "telegram_id INTEGER);"
                     "CREATE TABLE IF NOT EXISTS ВІДЛИВ("
                     "id INTEGER PRIMARY KEY,"
                     "Телефон TEXT,"
                     "Імя TEXT,"
                     "Відлив TEXT,"
                     "Колір TEXT,"
                     "Кількість INTEGER,"
                     "Довжина INTEGER,"
                     "В_роботі INTEGER,"
                     "telegram_id INTEGER);"
                     "CREATE TABLE IF NOT EXISTS МОСКІТКА("
                     "id INTEGER PRIMARY KEY,"
                     "Телефон TEXT,"
                     "Імя TEXT,"
                     "Тип TEXT,"
                     "Колір TEXT,"
                     "Кількість INTEGER,"
                     "Ширина INTEGER,"
                     "Довжина INTEGER,"
                     "В_роботі INTEGER,"
                     "telegram_id INTEGER);"
                     "CREATE TABLE IF NOT EXISTS ОСТЕКЛЕННЯ("
                     "id INTEGER PRIMARY KEY,"
                     "Телефон TEXT,"
                     "Імя TEXT,"
                     "Товщина TEXT,"
                     "Тип TEXT,"
                     "Кількість INTEGER,"
                     "Ширина INTEGER,"
                     "Довжина INTEGER,"
                     "В_роботі INTEGER,"
                     "telegram_id INTEGER);"
                     "CREATE TABLE IF NOT EXISTS ЖАЛЮЗІ("
                     "id INTEGER PRIMARY KEY,"
                     "Телефон TEXT,"
                     "Імя TEXT,"
                     "Тип TEXT,"
                     "Колір TEXT,"
                     "Управління TEXT,"
                     "Фіксація TEXT,"
                     "Кількість INTEGER,"
                     "Ширина INTEGER,"
                     "Довжина INTEGER,"
                     "telegram_id INTEGER,"
                     "В_роботі INTEGER);")
            self.cursor.executescript(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print("Помилка під час створення: ", Error)


    def __del__(self):
        self.cursor.close()
        self.connection.close()
