import pandas as pd
import pysqlite3

databaseFile = "../music.db"

instruments_file = '../instruments.csv'
names_file = '../names.txt'
inst_name_file = '../name_instrument.csv'

name_header = ['fname', 'lname']

DB = pysqlite3.connect(databaseFile)
cursor = DB.cursor()

# instDf = pd.read_csv(instruments_file, header=0, sep=",", engine='python')
# instDf.to_sql(name='Instruments', con=DB, if_exists='replace')
# print('Contents of Dataframe : ')
# print(instDf)
# sql = "SELECT * FROM `Instruments`"
# cursor.execute(sql)
# # Fetch all the records
# result = cursor.fetchall()
# for i in result:
#     print(i)
#
#
# combDf = pd.read_csv(inst_name_file, header=0, sep=",", engine='python')
# combDf.to_sql(name='Combined', con=DB, if_exists='replace')
# print('Contents of Dataframe : ')
# print(combDf)
# sql = "SELECT * FROM `Combined`"
# cursor.execute(sql)
# # Fetch all the records
# result = cursor.fetchall()
# for i in result:
#     print(i)


namesDf = pd.read_csv(names_file, header=None, sep='[,\s][ ]*', engine='python')
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
