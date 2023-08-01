from os import path
from sqlite3 import connect
from tkinter import messagebox


# Defining the path to the database.
current_file_path = path.abspath(__file__)
db_name = "db_statistics.db"
file_path = path.join(path.dirname(current_file_path), db_name)


def start_sql():
    """
    Creates and runs a database, 
    which contains a table 'statistics'.
    """
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


def add_to_database(date_value, time_value, tournament_name, buy_in, \
    quantity_buy_in, player_count, tournament_place, gain):
    """
    Takes 8 variables as arguments
    (called through the method 'get_value()' from the 'MyEntry' class)
    and saves them to a database table
    """
    with connect(file_path) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS statistics (\
        date_value TEXT, time_value TEXT, tournament_name TEXT,\
        buy_in REAL, quantity_buy_in INTEGER, \
        player_count INTEGER, tournament_place INTEGER, gain REAL)")
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
    """
    Selects all the data from the table, and returns it as a tuple
    """
    with connect(file_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM statistics")
        records = cursor.fetchall()
        employee_tuples_list = [tuple(record) for record in records]
        return employee_tuples_list


def get_total_tournament():
    """
    Selects data from the 'tournament_name' column 
    and returns the sum of the values of all cells in the column
    """
    with connect(file_path) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(tournament_name) FROM statistics')
        sum_result = cursor.fetchone()[0]
        if sum_result:
            return sum_result
        else:
            return 0


def count_buy_in():
    """
    Selects data from the 'quantity_buy_in' column
    and returns the sum of the values of all cells in the column
    """
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
    """
    Selects data from the 'gain' column
    and returns the sum of the values of all cells in the column
    """
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
    """
    Selects data from the 'buy_in' column
    and returns the sum of the values of all cells in the column
    """
    with connect(file_path) as connection:
        cursor = connection.cursor()
        sql_query = "SELECT SUM(buy_in) FROM statistics;"
        cursor.execute(sql_query)
        sum_result = cursor.fetchone()[0]
        if sum_result:
            return sum_result
        else:
            return 0


def full_cleaning():
    """
    Completely clears the table
    """
    with connect(file_path) as connection:
        cursor = connection.cursor()
        sql_query = "DELETE FROM statistics;"
        cursor.execute(sql_query)
        connection.commit()
        print("The table has been successfully cleared...")
        connection.commit()


# Variables in which the results of function execution are stored.
table_data = tuple_selection()
total_money_lose = float(count_money_lose())
total_money_win = float(count_money_win())
total_buy_in = int(count_buy_in())
total_tournament = int(get_total_tournament())