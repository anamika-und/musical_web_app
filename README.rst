DevOps: Dockerized Python Weather App
=====================================

Context and Description
-----------------------

The task is to create an API, written in Python3 that returns a
variety of data when GET calls are made to the endpoints specified below.
Your API should be containerized for ease of use and well documented.
Frameworks can be used if needed. Also, include tests to validate calls
to your endpoints return correctly. The final API code should be packaged
in a Docker container.

API Endpoints
-------------

====== ================ =================================================================
Method Endpoint         Description
====== ================ =================================================================
GET    /api/v1/datetime returns the current time and date (UTC or local)
GET    /api/v1/weather  returns the current weather for a given zip code (details below)
====== ================ =================================================================

Criteria for Success
--------------------
Ensure the app meets the following criteria:

* Add basic authentication to your API (you may hard-code credentials)
* The weather check should accept a minimal request with the following query arguments: :code:`GET /api/v1/weather?zip={zipcode,countrycode}&units={units}`

  .. list-table::
    :header-rows: 1
    :widths: 12 112

    * - Argument
      - Description
    * - zip
      - US Zip code or ISO 3166-1 Alpha-2 formatted country code.
    * - units
      - Unit of measure for temperature. Will be one of :code:`celsius`, :code:`farenheit`, or :code:`kelvin`.  OR, you
        may abbreviate units as :code:`C`, :code:`F`, or :code:`K`.

  The returned JSON blob must include the following fields, though additional fields may be returned:

  .. list-table::
    :header-rows: 1
    :widths: 12 12 112

    * - Property
      - Type
      - Description
    * - temperature
      - Number
      - The current temperature at the location specified by :code:`zip` in the units specified by :code:`units`.
    * - description
      - String
      - A human-readable summary of the current weather such as :code:`sunny`, :code:`cloudy`, or :code:`rainy`.
* Write your code in Python3 and document it well
* Containerize your code with Docker -- should be able
  run 'docker-compose up' to bring the API up to test it
* Make the API  handle errors gracefully and return error codes and messages
  that are easy to interpret
* Create a good set of tests with a testing framework that checks API endpoints for
  expected results in normal and error conditions.
* Return all data as JSON
* Add API documentation in OpenAPI / Swagger / ReDoc spec.
    * To fetch the OpenAPI swagger, simply make the following request:
      http://127.0.0.1:5000/apidocs/#/
    * Here, :code:`/apidocs` is the endpoint generated automatically by Flasgger API.
    * It generates the swagger spec by reading through the docstring of the route methods.
* Add a reverse web proxy on the front end (in another container)

Running the Weather App
-----------------------

To run the app outside a docker container, run the following command at the
project root:

:code:`python weather_app.py`

The app will run on :code:`http://127.0.0.1:5000/api/v1/` with endpoints set
up as :code:`/weather?zip=30318,us&units=celsius` for fetching current weather
and :code:`/datetime` for getting the current datetime. We can play around with
the zip, country code and units to get different results.

Dockerizing and testing the App
-------------------------------
The reverse proxy is configured using the :code:`nginx` reverse proxy. To start both the
containers i.e :code:`nginx` and our flask weather_app, simply run the following command:

:code:`docker-compose up -d nginx`

This will build the weather_app image and start both the :code:`weather_app` container as
well as :code:`nginx`.

To test the running weather application using our reverse proxy, run the following https
requests:

* http://localhost/api/v1/weather?zip=30318,us&units=celsius
* http://localhost/api/v1/datetime
* http://localhost/apidocs/#/ - to get the swagger Open API documentation.

The first two endpoints are secured via basic authentication (including the default root path
:code:`/`). Therefore, please use the following credentials to authenticate the requests:

:code:`username: anamika, password: learnDevOps`