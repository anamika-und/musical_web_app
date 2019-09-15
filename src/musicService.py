import sqlite3
from sqlite3 import Error
import os
import csv
import pandas as pd

from processData import process_names

""" connection variable for the SQLite database """
conn = None

""" SQLite database file """
databaseFile = "../music.db"

""" data files for SQLite database """
instruments_file = '../instruments.csv'
names_file = '../names.csv'
inst_name_file = '../name_instrument.csv'

""" Clear music.db if it exists """
if os.path.exists('databaseFile'):
    os.remove('databaseFile')


def get_connection():
    """ create a database connection to the SQLite database """
    try:
        global conn
        if conn is None:
            conn = sqlite3.connect(databaseFile)
            print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


def create_name_table(cur):
    """ create names table into the SQLite database """
    try:
        process_names()
        cur.execute("CREATE TABLE Names ("
                    "first_name TEXT NOT NULL PRIMARY KEY, "
                    "last_name);")  # use your column names here

        with open(names_file, 'r') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['first_name'], i['last_name']) for i in dr]

        sql = "INSERT INTO Names (first_name, last_name) VALUES (?, ?);"
        insert(cur, sql, to_db)
    except Error as e:
        print(e)


def create_instrument_table(cur):
    """ create instruments table into the SQLite database """
    try:
        cur.execute("CREATE TABLE Instruments ("
                    "Instrument TEXT NOT NULL PRIMARY KEY, "
                    "Section);")  # use your column names here

        with open(instruments_file, 'r') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['Instrument'], i['Section']) for i in dr]

        sql = "INSERT INTO Instruments (Instrument, Section) VALUES (?, ?);"
        insert(cur, sql, to_db)
    except Error as e:
        print(e)


def create_combined_table(cur):
    """ create combined table into the SQLite database """
    try:
        cur.execute("CREATE TABLE Combined ("
                    "Instrument TEXT NOT NULL, "
                    "Name TEXT NOT NULL, "
                    "FOREIGN KEY (Instrument) "
                    "REFERENCES Instruments (Instrument));")  # use your column names here

        with open(inst_name_file, 'r') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['Instrument'], i['Name']) for i in dr]

        sql = "INSERT INTO Combined (Instrument, Name) VALUES (?, ?);"
        insert(cur, sql, to_db)
    except Error as e:
        print(e)


def insert(cur, sql, to_db):
    """ insert data into a table in the SQLite database """
    try:
        cur.executemany(sql, to_db)
    except Error as e:
        print(e)


""" Make a convenience function for running SQL queries """


def sql_query():
    cur = get_connection().cursor()
    query = "SELECT a.Name, a.Instrument, b.Section from Combined as a join Instruments as b where a.Instrument = " \
            "b.Instrument; "
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    return rows


def sql_query2(query, var):
    cur = get_connection().cursor()
    cur.execute(query, var)
    rows = cur.fetchall()
    return rows


@app.before_request
def before_request():
    cur = get_connection().cursor()
    create_name_table(cur)
    create_instrument_table(cur)
    create_combined_table(cur)
    conn.commit()  # commit needed


@app.after_request
def after_request(response):
    conn.close()
    # return response


# if __name__ == '__main__':
#     # create_connection(r"../music.db")
#     conn = get_connection()
#     cur = conn.cursor()
#     create_name_table()
#     create_instrument_table()
#     create_combined_table()
#     conn.commit()  # commit needed
#     # PRAGMA table_info(names)
#     # select()
#     sql_query()
#     cur.close()
