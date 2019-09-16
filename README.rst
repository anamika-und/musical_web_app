DevOps: Music Web Application
=====================================

Context and Description
-----------------------
The task is to create a web application using the python flask API, and a SQLite database (a file).
Using the three files (names.txt, instruments.csv, and name_instrument.csv):

* Parses and loads the Names into one table, and the Instruments into another table.

* Note, when commas exist in the names.txt file, they separate "last, first". Otherwise, it's "first last".

* Parses and loads the name_instrument.csv file, and create database-level associations between the Instruments, and the characters playing those instruments.


Then, using your framework, please create a "homepage" that is a list of the following reports. When clicking on these links, the user should be prompted to download a csv file.

* A file showing the name, instrument, and section for all musicians.

* A file showing the instruments that don't yet have musicians (i.e. no one plays the trumpet), and their sections, sorted by section, alphabetically in ascending order.

* A file showing any musicians that play two or more instruments, their instrument, and section.

* A file showing any instruments that are played by multiple musicians, as well as the musician names and sections.


API Endpoints
-------------

====== ============================================ =======================================================================================
Method Endpoint                                     Description
====== ============================================ =======================================================================================
GET    /api/v1/musicians/data                       Returns the Name, Instruments and Section for all musicians
GET    /api/v1/instruments/no-musicians/data        Returns Instruments and Section that don't have any musicians
GET    /api/v1/musicians/multiple-instruments/data  Returns Names, Instruments and Section of musicians who play more than one instruments
GET    /api/v1/instruments/multiple-musicians/data  Returns Instruments, Name and Section for instruments played by multiple musicians
====== ============================================ =======================================================================================


Running the Musical App
-----------------------

To run the app, run the following command at the project root:

:code:`python musicApp.py`

The app will run on

:code:`http://127.0.0.1:5000/`