from os import path
from sqlite3 import connect
from tkinter import messagebox


current_file_path = path.abspath(__file__)
db_name = "db_statistics.db"
file_path = path.join(path.dirname(current_file_path), db_name)


def start_sql():
    """Создаёт и запускает базу данных, к оторой находится таблица statistics"""
    with connect(file_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS statistics (
                    date_value DATE,
                    time_value TIME,
                    tournament_name TEXT,
                    buy_in INT,
                    quantity_buy_in INT,
                    player_count INT,
                    tournament_place INT, 
                    gain FLOAT
            )""")

    print("Connection database...")
    connection.commit()


def add_to_database(date_value, time_value, tournament_name, buy_in, quantity_buy_in, player_count, tournament_place, gain):
    """Принимает в качестве аргументов 8 переменных(вызванных через метод get_value())
    и сохраняет их в таблицу базы данных"""
    with connect(file_path) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS statistics (date_value TEXT, time_value TEXT, tournament_name TEXT, buy_in REAL, quantity_buy_in INTEGER, player_count INTEGER, tournament_place INTEGER, gain REAL)")
        cursor.execute("INSERT INTO statistics VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
            date_value,
            time_value,
            tournament_name,
            buy_in,
            quantity_buy_in,
            player_count,
            tournament_place,
            gain
        ))
        print("Value added...")
        messagebox.showinfo('CONSERVATION', "RECORD SAVED")
        connection.commit()


def tuple_selection():
    """Выбирает все данные из таблицы, и возвращает их в виде картежа"""
    with connect(file_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM statistics")
        records = cursor.fetchall()
        employee_tuples_list = [tuple(record) for record in records]
        return employee_tuples_list


def get_total_tournament():
    """Выбирает данные из колонки tournament_name 
    и возвращает сумму значений всех ячеек в колонке"""
    with connect(file_path) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(tournament_name) FROM statistics')
        sum_result = cursor.fetchone()[0]
        if sum_result:
            return sum_result
        else:
            return 0


def count_buy_in():
    """Выбирает данные из колонки quantity_buy_in
    и возвращает сумму значений всех ячеек в колонке"""
    with connect(file_path) as connection:
        cursor = connection.cursor()
        sql_query = "SELECT SUM(quantity_buy_in) FROM statistics;"
        cursor.execute(sql_query)
        sum_result = cursor.fetchone()[0]
        if sum_result:
            return sum_result
        else:
            return 0


def count_money_win():
    """Выбирает данные из колонки gain
    и возвращает сумму значений всех ячеек в колонке"""
    with connect(file_path) as connection:
        cursor = connection.cursor()
        sql_query = "SELECT SUM(gain) FROM statistics;"
        cursor.execute(sql_query)
        sum_result = cursor.fetchone()[0]
        if sum_result:
            return sum_result
        else:
            return 0


def count_money_lose():
    """Выбирает данные из колонки buy_in
    и возвращает сумму значений всех ячеек в колонке"""
    with connect(file_path) as connection:
        cursor = connection.cursor()
        sql_query = "SELECT SUM(buy_in) FROM statistics;"
        cursor.execute(sql_query)
        sum_result = cursor.fetchone()[0]
        if sum_result:
            return sum_result
        else:
            return 0

table_data = tuple_selection()
total_money_lose = float(count_money_lose())
total_money_win = float(count_money_win())
total_buy_in = int(count_buy_in())
total_tournament = int(get_total_tournament())