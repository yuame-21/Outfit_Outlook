import unittest
from unittest.mock import MagicMock, patch
from src.connect_API import APIService
from src.ViewModel import Liner


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
        mock_response.json.return_value = {"current": {"temp": "25"}, "location": {"city": "Test City"} }
        self.mock_api_service.fetch_data.return_value = mock_response

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

    def test_curr_weather(self):
        self.liner.data = {"current": {"temp": "25", "humidity": "78"}, "location": {"city": "Test City"}}

        # test fetching temp
        self.assertEqual(self.liner.curr_weather("temp"), "25")

        # test fetching humidity
        self.assertEqual(self.liner.curr_weather("humidity"), "78")

    def test_location(self):
        self.liner.data = {"current": {"temp": "25", "humidity": "78"}, "location": {"city": "Test City",
                                                                                     "country": "Test Country"}}
        # test fetching city
        self.assertEqual(self.liner.location("city"), "Test City")

        # test fetching country
        self.assertEqual(self.liner.location("country"), "Test Country")

    def test_forecast(self):
        self.liner.data = {"forecast": {"weather": "sunny", "max_temp": "80"}, "current": {"temp": "25", "humidity": "78"},
                           "location": {"city": "Test City", "country": "Test Country"}}
        # test fetching city
        self.assertEqual(self.liner.forecast("weather"), "sunny")

        # test fetching country
        self.assertEqual(self.liner.forecast("max_temp"), "80")


if __name__ =="__main__":
    unittest.main()