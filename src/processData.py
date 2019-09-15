import re
import sqlite3
import pandas as pd

databaseFile = "../music.db"

instruments_file = '../instruments.csv'
input_names_file = '../names.txt'
output_names_file = '../names.csv'
inst_name_file = '../name_instrument.csv'
reg_ex = '; |, |\\*|\n'
name_header = ['first_name', 'last_name']


def process_names():
    """
    Opening, reading name file and building name array.
    """
    with open(input_names_file, 'r') as data:
        plaintext = data.read()
    name_array = plaintext.split('\n')

    # Final name list
    final_name_list = []

    # Parsing different name formats and standardizing to create csv
    for name in name_array:
        if len(name.split(',')) == 2:
            temp_name_list = re.split(reg_ex, name)
            last_name = temp_name_list.pop()
            first_name = temp_name_list.pop()
            final_name_list.append(last_name + ',' + first_name)
        elif len(name.split(' ')) == 2:
            final_name_list.append(name.replace(' ', ','))
        elif len(name.split(' ')) == 3:
            temp_name_list = re.split(' ', name)
            last_name = temp_name_list.pop()
            middle_name = temp_name_list.pop()
            first_name = temp_name_list.pop()
            final_name_list.append(first_name + ',' + middle_name + ' ' + last_name)
        else:
            final_name_list.append(name)

    # Writing final name list to a file
    with open(output_names_file, "w") as txt_file:
        for name in final_name_list:
            txt_file.write(name + "\n")  # works with any number of elements in a line

    names_df = pd.read_csv(output_names_file, names=name_header, sep=',', engine='python')
