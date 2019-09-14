#import os
import unittest
import json
from musical import musicApp
# from musical.weather_app import weatherApp

TEST_USER = {'test': 'BeTestall'}


class TestMusicalApp(unittest.TestCase):

    ############################
    #    setup and teardown    #
    ############################

    # executed prior to each test
    def setUp(self):
        # creates a test client
        self.app = musicalApp.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        # check if debug is set as false
        self.assertEqual(musicApp.DEBUG, False)

    # executed after each test for clean up
    def tearDown(self):
        pass

    # response in bytes to json converter
    def bytes_to_json(self, response):
        self.json_response = response.data.decode('utf8').replace("'", '"')
        self.data = json.loads(self.json_response)
        return self.data

    ###############
    #    tests    #
    ###############

    def test_root_path(self):
        """
        Test root path with basic auth
        :rtype: HTTP response
        :returns: 200 OK
        """
        response = self.app.get('/', headers={'Authorization': 'Basic dGVzdDpCZVRlc3RhbGw='})
        self.assertEqual(response.status_code, 200)
        data = self.bytes_to_json(response)
        self.assertEqual(data['message'], "Welcome to the Weather App! Be Stateless!!")

    def test_root_path_authorization_missing(self):
        """
        Test root path without basic auth
        :rtype: HTTP response
        :exception: 401 Unauthorized
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 401)

    def test_current_weather_in_celsius(self):
        """
        Test current musical with temp in celsius -  with basic auth
        :rtype: HTTP response
        :returns: 200 OK
        """
        response = self.app.get('/api/v1/musical?zip=30318,us&units=celsius',
                                headers={'Authorization': 'Basic dGVzdDpCZVRlc3RhbGw='})
        self.assertEqual(response.status_code, 200)
        data = self.bytes_to_json(response)
        self.assertIn('unit', data)
        self.assertIn('temperature', data)
        self.assertIn('description', data)
        self.assertEqual(data['name'], 'Atlanta')
        self.assertEqual(data['unit'], 'celsius')

    def test_current_weather_in_fahrenheit(self):
        """
        Test current musical with temp in fahrenheit -  with basic auth
        :rtype: HTTP response
        :returns: 200 OK
        """
        response = self.app.get('/api/v1/musical?zip=30318,us&units=fahrenheit',
                                headers={'Authorization': 'Basic dGVzdDpCZVRlc3RhbGw='})
        self.assertEqual(response.status_code, 200)
        data = self.bytes_to_json(response)
        self.assertIn('unit', data)
        self.assertIn('temperature', data)
        self.assertIn('description', data)
        self.assertEqual(data['name'], 'Atlanta')
        self.assertEqual(data['unit'], 'fahrenheit')

    def test_current_weather_zip_missing(self):
        """
        Test current musical with zip missing -  with basic auth
        :rtype: HTTP response
        :returns: 400 Bad Request
        """
        response = self.app.get('/api/v1/musical?zip=us&units=celsius',
                                headers={'Authorization': 'Basic dGVzdDpCZVRlc3RhbGw='})
        self.assertEqual(response.status_code, 400)

    def test_current_weather_country_missing(self):
        """
        Test current musical with country code missing -  with basic auth
        :rtype: HTTP response
        :returns: 400 Bad Request
        """
        response = self.app.get('/api/v1/musical?zip=30318&units=celsius',
                                headers={'Authorization': 'Basic dGVzdDpCZVRlc3RhbGw='})
        self.assertEqual(response.status_code, 400)

    def test_current_weather_units_missing(self):
        """
        Test current musical with units missing -  with basic auth
        :rtype: HTTP response
        :returns: 400 Bad Request
        """
        response = self.app.get('/api/v1/musical?zip=30318,us&units=',
                                headers={'Authorization': 'Basic dGVzdDpCZVRlc3RhbGw='})
        self.assertEqual(response.status_code, 400)

    def test_current_weather_authorization_missing(self):
        """
        Test current musical without basic auth
        :rtype: None
        :exception: 401 Unauthorized
        """
        response = self.app.get('/api/v1/musical?zip=30318,us&units=')
        self.assertEqual(response.status_code, 401)

    def test_current_date_time(self):
        """
        Test current date time with basic auth
        :rtype: HTTP response
        :returns: 200 OK
        """
        response = self.app.get('/api/v1/datetime',
                                headers={'Authorization': 'Basic dGVzdDpCZVRlc3RhbGw='})
        self.assertEqual(response.status_code, 200)
        data = self.bytes_to_json(response)
        self.assertIn('date_time', data)

    def test_current_date_time_authorization_missing(self):
        """
        Test current date time without basic auth
        :rtype: HTTP response
        :exception: 401 Unauthorized
        """
        response = self.app.get('/api/v1/datetime')
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
