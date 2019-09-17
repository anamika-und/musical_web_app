# Imports
from flask import Flask, render_template, send_file

import os
import csv
import src.musicService as musicService
from src.config import DEBUG

# Creating a Flask app
app = Flask(__name__)
output_data_file = "report.csv"
output_musicians_file = os.path.abspath(output_data_file)


def create_csv_file(results):
    """ Creates the report csv file """
    with open(output_musicians_file, "w", newline='') as csv_file:
        csv_file_out = csv.writer(csv_file)
        for row in results:
            csv_file_out.writerow(row)
        csv_file.close()


@app.route('/')
def music_app_homepage():
    """ GET web app homepage- default route"""
    results = musicService.sql_query_get_musicians()
    msg = 'All musicians with their respective instruments and section:'
    return render_template('musicData.html', results=results, msg=msg)


@app.route('/api/v1/musicians/data', methods=['GET'])
def music_app_get_musicians():
    """ GET musicians - result for query 1 """
    results = musicService.sql_query_get_musicians()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_data_file,
                     cache_timeout=0, as_attachment=True)


@app.route('/api/v1/instruments/no-musicians/data', methods=['GET'])
def music_app_get_instruments():
    """ GET instrument with no musicians - result for query 2 """
    results = musicService.sql_query_get_instruments()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_data_file,
                     cache_timeout=0, as_attachment=True)


@app.route('/api/v1/musicians/multiple-instruments/data', methods=['GET'])
def music_app_get_multiple_instruments():
    """ GET musicians with multiple instruments - result for query 3 """
    results = musicService.sql_query_get_musicians_multi_instruments()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_data_file,
                     cache_timeout=0, as_attachment=True)


@app.route('/api/v1/instruments/multiple-musicians/data', methods=['GET'])
def music_app_get_multiple_musicians():
    """ GET instruments with multiple musicians - result for query 4 """
    results = musicService.sql_query_get_instruments_multi_musicians()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_data_file,
                     cache_timeout=0, as_attachment=True)


# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    musicService.create_update_database()
    app.run(debug=DEBUG, host='127.0.0.1')
