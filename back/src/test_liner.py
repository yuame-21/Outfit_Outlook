import unittest
from unittest.mock import MagicMock, patch
from back.src.connect_API import APIService
from back.src.ViewModel import Liner


class TestLiner(unittest.TestCase):
    def setUp(self):
        # we create a mock APIService to avoid real API calls during testing
        self.mock_api_service = MagicMock(spec=APIService)
        self.liner = Liner("test_loc")
        self.liner.api_service = self.mock_api_service

    def test_fetch_data_succ(self):
        # mock response for successful API call
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"current": {"temp": "25"}, "location": {"city": "Test City"}}
        self.mock_api_service.fetch_data.return_value = mock_response

        # simulate clean_data() of mock API service
        self.mock_api_service.clean_data.return_value = {"current": {"temp": "25"}, "location": {"city": "Test City"}}

        self.liner.fetch_data()

        # verify that self.data is updated with the mock API response
        self.assertEqual(self.liner.data, {"current": {"temp": "25"}, "location": {"city": "Test City"}})

    def test_fetch_data_fail(self):
        # mock response for failed API call
        mock_response = MagicMock()
        mock_response.status_code = 404
        self.mock_api_service.fetch_data.return_value = mock_response

        # suppress the print output to keep test reports clean
        with patch("builtins.print"):
            self.liner.fetch_data()

        # verify that self.data remains unchanged due to a failed API call
        self.assertEqual(self.liner.data, {})

    def test_parse(self):
        self.liner.data = {"current": {"temp": "25", "humidity": "78"},
                           "location": {"city": "Test City", "country": "Test Country"},
                           "forecast": {"condition": "sunny", "max_temp": "80"}}
        # test fetching current temp
        self.assertEqual(self.liner.parse_weather("current", "temp"), "25")

        # test fetching current humidity
        self.assertEqual(self.liner.parse_weather("current", "humidity"), "78")

        # test fetching location city
        self.assertEqual(self.liner.parse_weather("location", "city"), "Test City")

        # test fetching location country
        self.assertEqual(self.liner.parse_weather("location", "country"), "Test Country")

        # test fetching forecast condition
        self.assertEqual(self.liner.parse_weather("forecast", "condition"), "sunny")

        # test fetching forecast max temp
        self.assertEqual(self.liner.parse_weather("forecast", "max_temp"), "80")


if __name__ == "__main__":
    unittest.main()
