import sys

from database.connection import add_to_database, tuple_selection, table_data,\
total_money_lose, total_money_win, total_buy_in, total_tournament,\
count_money_win, get_total_tournament, count_money_lose, \
count_buy_in, full_cleaning
from other.user_help import info

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel


class MyLabel:
    """
    Creates a Label widget, accepting the parameters:
    1. windows - window where the widget will be located.
    2. text - text that will be specified in the widget.
    3. x and y - coordinates by which the widget will be located in the window.
    4. font - text parameters (size, font, ...)
    """
    def __init__(self, window, text, x, y, font):
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.label = tk.Label(self.window, text=self.text, font=self.font)
        self.label.place(x=self.x, y=self.y)


class MyEntry:
    """
    Creates Entry widget (input field) by taking parameters:
    1. windows - window in which the widget will be located.
    2. x and y - coordinates by which the widget will be located in the window.
    """
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.value = tk.StringVar()
        self.text = tk.Entry(self.window, textvariable=self.value)
        self.text.place(x=self.x, y=self.y)

    def get_value(self):
        """
        Method for retrieving values from the Entry field
        """
        return self.value.get()


class MyButton:
    """
    Creates a Button widget, taking parameters:
    1. windows - window in which the widget will be located.
    2. text - the text that will be specified to the button.
    3. command - name of the function that will be executed when clicked.
    4. x and y - coordinates, by which the widget will be located in the window.
    """
    def __init__(self, window, text, command, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.text = text
        self.command = command
        self.btn = tk.Button(self.window, text=self.text, command=self.command)
        self.btn.grid(column=0, row=0)
        self.btn.place(x=self.x, y=self.y)


# Creates the main window in the application.
basic_window = tk.Tk()
basic_window.geometry("485x210")
basic_window.title("poker_statics")


# Name of 'common' parameter values from columns in the table.
money_spent_0 = MyLabel(basic_window, " MONEY\nSPENT:", 105, 130, 'Times 10')
total_gain_0 = MyLabel(basic_window, " MONEY \nRECEIVED:", 100, 165, 'Times 10')
total_tournament_0 = MyLabel(basic_window, "TOURNAMENTS \n PLAYED:", 330, 130, 'Times 10')
total_buy_in_0 = MyLabel(basic_window, "NUMBER OF \n INPUTS:", 345, 165, 'Times 10')


def total_money_win():
    """
    Updates the data received from the function: count_money_win
    """
    data = float(count_money_win())
    return data
    basic_window.after(1000, total_money_win)


def total_tournament():
    """
    Updates the data received from the function: get_total_tournament
    """
    data = int(get_total_tournament())
    return data
    basic_window.after(1000, total_tournament)


def total_money_lose():
    """
    Updates the data received from the function: count_money_lose
    """
    data = float(count_money_lose())
    return data
    basic_window.after(1000, total_money_lose)


def total_buy_in():
    """
    Updates the data received from the function: count_buy_in
    """
    data = int(count_buy_in())
    return data
    basic_window.after(1000, total_buy_in)


def update_label():
    """
    Updates the 'label' widgets on the main window
    """
    money_spent_1 = MyLabel(basic_window, f"{total_money_win()} $", 160, 135, 'Times 15') 
    total_tournament_1 = MyLabel(basic_window, total_tournament(), 435, 135, 'Times 15') 
    total_gain_1 = MyLabel(basic_window, f"{total_money_lose()} $", 180, 170, 'Times 15') 
    total_buy_in_1= MyLabel(basic_window, total_buy_in(), 430, 170, 'Times 15') 
    basic_window.after(1000, update_label)

update_label()


# A 'label' widget describing the 'Entry' fields.
tournament_name_0 = MyLabel(basic_window, "TOURNAMENT NAME:", 5, 11, 'Times 10')
quantity_buy_in_0 = MyLabel(basic_window, "QUANTINTY BUY IN:", 16, 41, 'Times 10')
tournament_place_0 = MyLabel(basic_window, "TOURNAMENT PLACE:", 4, 71, 'Times 10')
player_count_0 = MyLabel(basic_window, "PLAYER COUNT:  ", 36, 101, 'Times 10')
date_value_0 = MyLabel(basic_window, "DATA:", 290, 11, 'Times 10')
time_value_0 = MyLabel(basic_window, "TIME:", 295, 41, 'Times 10')
buy_in_0 = MyLabel(basic_window, "BUY IN:", 285, 71, 'Times 10')
gain_0 = MyLabel(basic_window, "GAIN:", 295, 101, 'Times 10')


# Fields for entering 'Entry' information
tournament_name_1 = MyEntry(basic_window, 150, 12)
quantity_buy_in_1 = MyEntry(basic_window, 150, 42)
tournament_place_1 = MyEntry(basic_window, 150, 72)
player_count_1 = MyEntry(basic_window, 150, 102)
date_value_1 = MyEntry(basic_window, 340, 12)
time_value_1 = MyEntry(basic_window, 340, 42)
buy_in_1 = MyEntry(basic_window, 340, 72)
gain_1 = MyEntry(basic_window, 340, 101)


def open_statistics(data):
    """
    Creates a window that contains a table,
    consisting of 8 columns, the information in which comes from the
    'statistics' table of the database
    """
    statistics = Toplevel()
    statistics.geometry("970x400")
    statistics.title("Statistics")
    statistics.resizable(width=False, height=False) 


    def update():
        """
        Updates the data coming from the function: tuple_selection
        """
        data = tuple_selection()
        return data
        statistics.after(1000, update)


    def sort_column(tree, col, reverse):
        """
        Adds the ability to sort the table by columns
        """
        data = [(float(tree.set(child, col)), child) \
        for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for index, (value, child) in enumerate(data):
            tree.move(child, '', index)
        tree.heading(col, command=lambda: sort_column(tree, col, not reverse))


    def update_statistics():
        """
        Deletes rows and columns from the statistics
        window and replaces them with new ones, thus 
        updating the information in them
        """
        table.delete(*table.get_children())
        for row in update():
            table.insert('', tk.END, values=row)
        statistics.after(1000, update_statistics)


    # Creates column names in a table.
    heads = ["DATE VALUE", "TIME VALUE", "TOURNAMENT NAME", "BUY-IN",\
    "QUANTITY BUY-IN", "PLAYER COUNT", "TOURNAMENT PLACE", "GAIN"] 
    table = ttk.Treeview(statistics, show="headings")  
    table["columns"] = heads
    

    # Assigns column names to the table.
    for header in heads:
        table.heading(header, text=header, anchor="center",\
        command=lambda col=header: sort_column(table, col, False))
        table.column(header, anchor="center", width=100)


    # Adds scrolling capability to a table.
    scrollpane = ttk.Scrollbar(statistics, command=table.yview)
    scrollpane.pack(side=tk.RIGHT, fill=tk.Y)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    table.configure(yscrollcommand=scrollpane.set)

    update_statistics()


def add_value_to_database():
    """
    Activates the 'add_to_database' function, 
    which takes values from the 'Entry' fields and 
    enters them into the database table via the 'get_value' method
    """
    add_to_database(
    date_value_1.get_value(), 
    time_value_1.get_value(), 
    tournament_name_1.get_value(),
    buy_in_1.get_value(), 
    quantity_buy_in_1.get_value(), 
    player_count_1.get_value(), 
    tournament_place_1.get_value(), 
    gain_1.get_value())


def show_statistics():
    """
    Открывает окно со статистикой(таблица) 
    и подгружает в неё данные из базы данных 'db_statistics'.
    """
    open_statistics(table_data)


def information():
    """
    Popup window with instructions on how to fill out the form for the user. 
    The function belongs to the 'information' button.
    """
    messagebox.showinfo('FIELD FORMAT.', info)


def clean():
    """
    Displays a warning window, with an option to clear the table completely.
    """
    choice = messagebox.askyesno("CLEAN", "Do you really\
 want to completely clear the table ?")
    if choice:
        full_cleaning()
        messagebox.showinfo("CLEAN", "The table has been\
 cleared!\nPlease restart the program")


# Button output block on the main window.
btn_save = MyButton(basic_window, "SAVE", add_value_to_database, 8, 140)
btn_statistics = MyButton(basic_window, "STATISTICS", show_statistics, 7, 170)
information = MyButton(basic_window, "?", information, 10, 100)
btn_clean = MyButton(basic_window, "♻️", clean, 50, 140)


def start_gui():
	"""
    GUI startup function
    """
	basic_window.mainloop()