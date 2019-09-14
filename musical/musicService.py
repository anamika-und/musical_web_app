import sqlite3
from sqlite3 import Error
import os
import pandas as pd

""" connection variable for the SQLite database """
conn = None

databaseFile = "../music.db"

instruments_file = '../instruments.csv'
header_instruments = ['Instrument', 'Section']

df = pd.read_csv(instruments_file, header=0, sep=",")

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


def create_name_table():
    """ create names table into the SQLite database """
    try:
        name_sql = """CREATE TABLE NAMES (fname text PRIMARY KEY, lname text NOT NULL) """
        cur.execute(name_sql)
    except Error as e:
        print(e)


def create_instrument_table():
    """ create instruments table into the SQLite database """
    try:
        instrument_sql = """CREATE TABLE INSTRUMENTS (INSTRUMENT text PRIMARY KEY, SECTION text NOT NULL) """
        cur.execute(instrument_sql)
    except Error as e:
        print(e)


def create_combined_table():
    """ create combined table into the SQLite database """
    try:
        combined_sql = """CREATE TABLE COMBINED (INSTRUMENT text PRIMARY KEY, first_name text NOT NULL, last_name 
        text NOT NULL) """
        cur.execute(combined_sql)
    except Error as e:
        print(e)


def insert():
    """ insert data into a table in the SQLite database """
    try:
        names_sql = "INSERT INTO NAMES (first_name, last_name) VALUES (?, ?)"
        cur.execute(names_sql, ('AB', 'CD'))
        cur.execute(names_sql, ('EF', 'GH'))
    except Error as e:
        print(e)


""" Make a convenience function for running SQL queries """


def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


def sql_edit_insert(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()


def sql_delete(query, var):
    cur = conn.cursor()
    cur.execute(query, var)


def sql_query2(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    rows = cur.fetchall()
    return rows


# @app.before_request
# def before_request():
#     get_connection()
#
#
# @app.after_request
# def after_request(response):
#     conn.close()
#     return response


if __name__ == '__main__':
    # create_connection(r"../music.db")
    conn = get_connection()
    cur = conn.cursor()
    create_name_table()
    create_instrument_table()
    create_combined_table()
    insert()
    conn.commit()  # commit needed
    # PRAGMA table_info(names)
    # select()
    cur.close()

# conn = get_db()
# c = conn.cursor()
#
# read_names = pd.read_csv(r'./names.txt')
# read_names.to_sql('NAMES', conn, if_exists='append',
#                     index=False)  # Insert the values from the txt file into the table 'NAMES'
#
# read_instruments = pd.read_csv(r'./instruments.csv')
# read_instruments.to_sql('INSTRUMENTS', conn, if_exists='replace',
#                     index=False)  # Replace the values from the csv file into the table 'INSTRUMENTS'

# When reading the csv:
# - Place 'r' before the path string to read any special characters, such as '\'
# - Don't forget to put the file name at the end of the path + '.csv'
# - Before running the code, make sure that the column names in the CSV files match with the column names in the tables created and in the query below
# - If needed make sure that all the columns are in a TEXT format

# c.execute('''
# INSERT INTO DAILY_STATUS (Client_Name,Country_Name,Date)
# SELECT DISTINCT clt.Client_Name, ctr.Country_Name, clt.Date
# FROM CLIENTS clt
# LEFT JOIN COUNTRY ctr ON clt.Country_ID = ctr.Country_ID
#           ''')
#
# c.execute('''
# SELECT DISTINCT *
# FROM DAILY_STATUS
# WHERE Date = (SELECT max(Date) FROM DAILY_STATUS)
#           ''')

# print(c.fetchall())

# df = DataFrame(c.fetchall(), columns=['Client_Name', 'Country_Name', 'Date'])
# print(
#     df)  # To display the results after an insert query, you'll need to add this type of syntax above: 'c.execute(''' SELECT * from latest table ''')

# df.to_sql('DAILY_STATUS', conn, if_exists='append',
#           index=False)  # Insert the values from the INSERT QUERY into the table 'DAILY_STATUS'

# export_csv = df.to_csv (r'C:\Users\Ron\Desktop\Client\export_list.csv', index = None, header=True) # Uncomment this syntax if you wish to export the results to CSV. Make sure to adjust the path name
# Don't forget to add '.csv' at the end of the path (as well as r at the beg to address special characters)