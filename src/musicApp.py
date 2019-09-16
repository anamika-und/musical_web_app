# Imports
from flask import Flask, render_template, send_file

import csv
import musicService
from src.config import DEBUG

# Creating a Flask app
app = Flask(__name__)
output_musicians_file = 'musicians.csv'


def create_csv_file(results):
    with open(output_musicians_file, "w", newline='') as csv_file:
        csv_file_out = csv.writer(csv_file)
        for row in results:
            csv_file_out.writerow(row)
        csv_file.close()


@app.route('/')
def music_app_homepage():
    results = musicService.sql_query_get_musicians()
    msg = 'All musicians with their respective instruments and section:'
    return render_template('musicData.html', results=results, msg=msg)


@app.route('/api/v1/musicians/data', methods=['GET'])
def music_app_get_musicians():
    results = musicService.sql_query_get_musicians()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_musicians_file)


@app.route('/api/v1/instruments/no-musicians/data', methods=['GET'])
def music_app_get_instruments():
    results = musicService.sql_query_get_instruments()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_musicians_file)


@app.route('/api/v1/musicians/multiple-instruments/data', methods=['GET'])
def music_app_get_multiple_instruments():
    results = musicService.sql_query_get_musicians_multi_instruments()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_musicians_file)


@app.route('/api/v1/instruments/multiple-musicians/data', methods=['GET'])
def music_app_get_multiple_musicians():
    results = musicService.sql_query_get_instruments_multi_musicians()
    create_csv_file(results)
    return send_file(output_musicians_file, mimetype='text/csv', attachment_filename=output_musicians_file)


# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    app.run(debug=DEBUG, host='127.0.0.1')
