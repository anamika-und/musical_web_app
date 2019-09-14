import re
import sqlite3
import pandas as pd

databaseFile = "../music.db"

instruments_file = '../instruments.csv'
names_file = '../names.txt'
output_names_file = '../output.txt'
inst_name_file = '../name_instrument.csv'
reg_ex = '; |, |\\*|\n'
name_header = ['first_name', 'last_name']

DB = sqlite3.connect(databaseFile)
cursor = DB.cursor()

instDf = pd.read_csv(instruments_file, header=0, sep=",", engine='python')
instDf.to_sql(name='Instruments', con=DB, if_exists='replace')
print('Contents of Dataframe : ')
print(instDf)
sql = "SELECT * FROM `Instruments`"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)


combDf = pd.read_csv(inst_name_file, header=0, sep=",", engine='python')
combDf.to_sql(name='Combined', con=DB, if_exists='replace')
print('Contents of Dataframe : ')
print(combDf)
sql = "SELECT * FROM `Combined`"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

"""
Opening, reading name file and building name array.
"""
with open(names_file, 'r') as data:
    plaintext = data.read()
nameArray = plaintext.split('\n')

# Final name list
finalNameList = []

# Parsing different name formats and standardizing to create csv
for name in nameArray:
    tempNameList = list()
    if len(name.split(',')) == 2:
        tempNameList = re.split(reg_ex, name)
        last_name = tempNameList.pop()
        first_name = tempNameList.pop()
        finalNameList.append(last_name + ',' + first_name)
    elif len(name.split(' ')) == 2:
        tempNameList = re.split(reg_ex, name)
        finalNameList.append(name.replace(' ', ','))
    elif len(name.split(' ')) == 3:
        tempNameList = re.split(' ', name)
        last_name = tempNameList.pop()
        middle_name = tempNameList.pop()
        first_name = tempNameList.pop()
        finalNameList.append(first_name + ',' + middle_name + ' ' + last_name)
    else:
        finalNameList.append(name)

# Writing final name list to a file
with open(output_names_file, "w") as txt_file:
    for name in finalNameList:
        txt_file.write(name + "\n")  # works with any number of elements in a line

namesDf = pd.read_csv(output_names_file, header=None, sep=',', engine='python')
namesDf.columns = name_header
namesDf.to_sql(name='Names', con=DB, if_exists='replace')
print('Contents of Dataframe : ')
print(namesDf)
sql = "SELECT * FROM `Names`"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

DB.close()
