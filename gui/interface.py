import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


from database.connection import add_to_database, tuple_selection, table_data, total_money_lose, total_money_win, total_buy_in, total_tournament
from other.user_help import info


class MyLabel:

    """Создаёт виджет Lbel(надпись), принимая параметры:
    1. windows - окно в котором будет расположен виджет
    2. text - текст, который будет указан в виджете
    3. x и y - координаты, по которым будет расположен виджет в окне
    4. font - параметры текста (размер, шрифт, ...)"""
    def __init__(self, window, text, x, y, font):
        self.window = window
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.label = tk.Label(self.window, text=self.text, font=self.font)
        self.label.place(x=self.x, y=self.y)


class MyEntry:

    """Создаёт виджет Entry(поле для ввода), принимая параметры:
    1. windows - окно в котором будет расположен виджет.
    2. x и y - координаты, по которым будет расположен виджет в окне"""
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.value = tk.StringVar()
        self.text = tk.Entry(self.window, textvariable=self.value)
        self.text.place(x=self.x, y=self.y)
        
    def get_value(self):
        """Метод получения значений с поля для ввода Entry"""
        return self.value.get()


class MyButton:

    """Создаёт виджет Button(кнопка), принимая параметры:
    1. windows - окно в котором будет расположен виджет.
    2. text - текст, который будет указан кнопке.
    3. command - название функции, которая будет выполняться, при нажатии.
    4. x и y - координаты, по которым будет расположен виджет в окне"""
    def __init__(self, window, text, command, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.text = text
        self.command = command
        self.btn = tk.Button(self.window, text=self.text, command=self.command)
        self.btn.grid(column=0, row=0)
        self.btn.place(x=self.x, y=self.y)


"""Создание окна в приложении"""
basic_window = tk.Tk()
basic_window.geometry("475x210")
basic_window.title("poker_statics")


"""Название 'общих' значений параметров из колонок в таблице"""
money_spent_0 = MyLabel(basic_window, " MONEY\nSPENT:", 105, 130, 'Times 10')   # Label: MONEY SPENT.
total_gain_0 = MyLabel(basic_window, " MONEY \nRECEIVED:", 100, 165, 'Times 10')   # Label: MONEY RECEIVED.
total_tournament_0 = MyLabel(basic_window, "TOURNAMENTS \n PLAYED:", 330, 130, 'Times 10')   # Label: TOURNAMENTS PLAYED.
total_buy_in_0 = MyLabel(basic_window, "NUMBER OF \n INPUTS:", 345, 165, 'Times 10')   # Label: NUMBER OF INPUTS


"""Значение, передаваемые из БД, которые ссылаются на суммы значений колонок в таблице"""
money_spent_1 = MyLabel(basic_window, f"{total_money_win} $", 160, 135, 'Times 15')   # Label: MONEY SPENT.
total_tournament_1 = MyLabel(basic_window, total_tournament, 435, 135, 'Times 15')   # Label: TOURNAMENTS PLAYED.
total_gain_1 = MyLabel(basic_window, f"{total_money_lose} $", 180, 170, 'Times 15')   # Label: MONEY RECEIVED.
total_buy_in_1= MyLabel(basic_window, total_buy_in, 430, 170, 'Times 15')   # Label: NUMBER OF INPUTS


"""Названия полей для ввода"""
tournament_name_0 = MyLabel(basic_window, "TOURNAMENT NAME:", 5, 11, 'Times 10')   # Label: TOURNAMENT NAME
quantity_buy_in_0 = MyLabel(basic_window, "QUANTINTY BUY IN:", 16, 41, 'Times 10')   # Label: QUANTINTY BUY IN
tournament_place_0 = MyLabel(basic_window, "TOURNAMENT PLACE:", 4, 71, 'Times 10')   # Label: TOURNAMENT PLACE
player_count_0 = MyLabel(basic_window, "PLAYER COUNT:  ", 36, 101, 'Times 10')   # Label: PLAYER COUNT
date_value_0 = MyLabel(basic_window, "DATA:", 290, 11, 'Times 10')   # Label: DATA
time_value_0 = MyLabel(basic_window, "TIME:", 295, 41, 'Times 10')   # Label: TIME
buy_in_0 = MyLabel(basic_window, "BUY IN:", 285, 71, 'Times 10')   # Label: BUY IN
gain_0 = MyLabel(basic_window, "GAIN:", 295, 101, 'Times 10')   # Label: GAIN


"""Поля для ввода Entry"""
tournament_name_1 = MyEntry(basic_window, 150, 12)   # Поле для ввода от label: TOURNAMENT NAME
quantity_buy_in_1 = MyEntry(basic_window, 150, 42)   # Поле для ввода от label: QUANTINTY BUY IN
tournament_place_1 = MyEntry(basic_window, 150, 72)   # Поле для ввода от label: TOURNAMENT PLACE
player_count_1 = MyEntry(basic_window, 150, 102)   # Поле для ввода от label: PLAYER COUNT
date_value_1 = MyEntry(basic_window, 340, 12)   # Поле для ввода от label: DATA
time_value_1 = MyEntry(basic_window, 340, 42)   # Поле для ввода от label: TIME
buy_in_1 = MyEntry(basic_window, 340, 72)   # Поле для ввода от label: BUY IN
gain_1 = MyEntry(basic_window, 340, 101)   # Поле для ввода от label: GAIN



def open_statistics(data):
    """Создаёт окно, в котором располагается таблица,
    состоящая из 8 колонок, информация в которые, поступает из
    таблицы statistics базы данных"""
    statistics = tk.Tk()
    statistics.geometry("950x400")
    statistics.title("statics")
    statistics.resizable(width=False, height=False)

    heads = ["DATE VALUE", "TIME VALUE", "TOURNAMENT NAME", "BUY-IN", "QUANITY BUY_IN", "PLAYER COUNT", "TOURNAMENT PLACE", "GAIN"]   # Названпие колонок в таблице

    table = ttk.Treeview(statistics, show="headings")  
    table["columns"] = heads 
    for row in data:   
        table.insert('', tk.END, values=row)
    
    for headers in heads:
        table.heading(headers, text=headers, anchor="center")
        table.column(headers, anchor="center", width=100)

    scrollpane = ttk.Scrollbar(statistics, command=table.yview)
    scrollpane.pack(side=tk.RIGHT, fill=tk.Y)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    table.configure(yscrollcommand=scrollpane.set)


def add_value_to_database():
    """Активирует функцию 'add_to_database', которая берет значения с полей Entry и 
    заносит их в таблицу базы данных, через метод get_value()"""
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
    """Открывает окно со статистикой(таблица) и подгружает в неё данные из БД"""
    open_statistics(table_data)


def information():
    """Всплывающее окно, с инструкцией по заполнению формы для пользователя. 
    Функция принадлежит кнопке 'information'. """
    messagebox.showinfo('FIELD FORMAT.', info)

btn_save = MyButton(basic_window, "SAVE", add_value_to_database, 10, 135)   # Кнопка сохранения данных из полей в базу данных
btn_statistics = MyButton(basic_window, "STATISTICS", show_statistics, 7, 165)   # Кнопка открытия окна со статистикой (таблицекй).
information = MyButton(basic_window, "?", information, 55, 135)   # Кнопка с открытием всплываюбщего информационного окна для пользователя


def start_gui():
	"""Функция запуска графического интерфейса"""
	basic_window.mainloop()


