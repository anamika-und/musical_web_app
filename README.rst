DevOps: Music Web Application
=====================================

Context and Description
-----------------------
The task is to create a web application using the python flask API, and a SQLite database (a file).
Using the three files (names.txt, instruments.csv, and name_instrument.csv):
1. Parses and loads the Names into one table, and the Instruments into another table.
Note, when commas exist in the names.txt file, they separate "last, first".
Otherwise, it's "first last".
2. Parses and loads the name_instrument.csv file, and create database-level associations between
the Instruments, and the characters playing those instruments.

Then, using your framework, please create a "homepage" that is a list of the following reports.
When clicking on these links, the user should be prompted to download a csv file.
1. A file showing the name, instrument, and section for all musicians.
2. A file showing the instruments that don't yet have musicians (i.e. no one plays the trumpet),
and their sections, sorted by section, alphabetically in ascending order.
3. A file showing any musicians that play two or more instruments, their instrument, and section.
4. A file showing any instruments that are played by multiple musicians, as well as the musician
names and sections.

API Endpoints
-------------

====== ================ =================================================================
Method Endpoint         Description
====== ================ =================================================================
GET    /api/v1/
GET    /api/v1/
====== ================ =================================================================

Running the Musical App
-----------------------

To run the app outside a docker container, run the following command at the
project root:

:code:`python musicApp.py`

The app will run on :code:`http://127.0.0.1:5000/api/v1/` with endpoints set
up as :code:`/music` for fetching data from sqlite3
and :code:`/??????` for ???????. We can play around with