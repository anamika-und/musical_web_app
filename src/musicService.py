import csv
import os
import sqlite3
from sqlite3 import Error
import processData as processData

from musicApp import app

""" SQLite database file """
databaseFile = os.path.abspath("../music.db")

conn = None

""" data files for SQLite database """
instruments_file = os.path.abspath("../instruments.csv")
names_file = os.path.abspath("../names.csv")
inst_name_file = os.path.abspath("../name_instrument.csv")

""" Clear music.db if it exists """
if os.path.exists('databaseFile'):
    os.remove('databaseFile')


def get_connection():
    """ create a database connection to the SQLite database """
    try:
        global conn
        if conn is None:
            print('Creating a database connection ...')
            conn = sqlite3.connect(databaseFile)
            print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


def create_name_table(cur):
    """ create names table into the SQLite database """
    try:
        print('Processing names.txt ...')
        processData.process_names()
        print('Creating table Names ...')
        cur.execute("CREATE TABLE Names ("
                    "first_name TEXT NOT NULL PRIMARY KEY, "
                    "last_name);")  # use your column names here

        with open(names_file, 'r') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['first_name'], i['last_name']) for i in dr]
        print('Inserting names ...')
        sql = "INSERT INTO Names (first_name, last_name) VALUES (?, ?);"
        insert(cur, sql, to_db)
    except Error as e:
        print(e)


def create_instrument_table(cur):
    """ create instruments table into the SQLite database """
    try:
        print('Creating table Instruments ...')
        cur.execute("CREATE TABLE Instruments ("
                    "Instrument TEXT NOT NULL PRIMARY KEY, "
                    "Section);")  # use your column names here

        with open(instruments_file, 'r') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['Instrument'], i['Section']) for i in dr]
        print('Inserting data into table Instruments ...')
        sql = "INSERT INTO Instruments (Instrument, Section) VALUES (?, ?);"
        insert(cur, sql, to_db)
    except Error as e:
        print(e)


def create_combined_table(cur):
    """ create combined table into the SQLite database """
    try:
        print('Creating table Combined ...')
        cur.execute("CREATE TABLE Combined ("
                    "Instrument TEXT NOT NULL, "
                    "Name TEXT NOT NULL, "
                    "FOREIGN KEY (Instrument) "
                    "REFERENCES Instruments (Instrument));")  # use your column names here

        with open(inst_name_file, 'r') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['Instrument'], i['Name']) for i in dr]
        print('Inserting data into table Combined ...')
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


def sql_query_get_musicians():
    """ QUERY: 1"""
    cur = get_db_connection()
    query = "SELECT a.Name, a.Instrument, b.Section from Combined as a join Instruments as b where a.Instrument = " \
            "b.Instrument; "
    cur.execute(query)
    rows = cur.fetchall()
    rows.sort()
    print(rows)
    return rows


def sql_query_get_instruments():
    """ QUERY: 2"""
    cur = get_db_connection()
    query = "SELECT a.Section, a.Instrument FROM Instruments a LEFT JOIN Combined b ON a.Instrument = b.Instrument " \
            "WHERE b.Instrument IS NULL; "
    cur.execute(query)
    rows = cur.fetchall()
    rows.sort()
    print(rows)
    return rows


def sql_query_get_musicians_multi_instruments():
    """ QUERY: 3"""
    cur = get_db_connection()
    query = "Select a.Name, a.Instrument, c.Section from Combined a inner join Combined b on a.Name = b.Name and " \
            "a.Instrument != b.Instrument left join Instruments c on b.Instrument = c.instrument; "
    cur.execute(query)
    rows = cur.fetchall()
    rows.sort()
    print(rows)
    return rows


def sql_query_get_instruments_multi_musicians():
    """ QUERY: 4"""
    cur = get_db_connection()
    query = "Select DISTINCT a.Instrument, a.Name, c.Section from Combined a INNER JOIN Combined b on a.Instrument = " \
            "b.Instrument and a.Name != b.Name JOIN Instruments c on b.Instrument = c.instrument; "
    cur.execute(query)
    rows = cur.fetchall()
    rows.sort()
    print(rows)
    return rows


def get_db_connection():
    query_conn = sqlite3.connect(databaseFile)
    cur = query_conn.cursor()
    return cur


def create_update_database():
    get_connection()
    cur = conn.cursor()
    create_name_table(cur)
    create_instrument_table(cur)
    create_combined_table(cur)
    conn.commit()  # commit needed


@app.after_request
def after_request():
    get_connection().close()
