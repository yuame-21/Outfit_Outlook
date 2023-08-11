import unittest
from unittest.mock import MagicMock, patch
from back.src.connect_API import APIService
import requests


# test APIService data fetching function and data cleaning function
class TestAPIService(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        api_service = APIService("test_loc")
        response = api_service.fetch_data()

        self.assertEqual(response, mock_response)
        mock_get.assert_called_once_with(
            'http://api.weatherapi.com/v1/forecast.json?key=7bbdace306904520a56214618232605&q=test_loc&aqi=no'
        )

    def test_clean_data(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "location": {
                "name": "loc",
                "region": "loc, loc",
                "country": "UK",
            },
            "current": {
                "temp_f": 73.4,
                "condition": {
                    "text": "Partly cloudy",
                    "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
                    "code": 1003
                },
                "wind_mph": 9.4,

            },
            "forecast": {
                "forecastday": [
                    {
                        "date": "2023-08-10",
                        "date_epoch": 1691625600,
                        "day": {
                            "maxtemp_c": 26.3,
                            "maxtemp_f": 79.3,
                            "mintemp_c": 16.0,
                            "mintemp_f": 60.8,
                            "avgtemp_c": 21.1,
                            "avgtemp_f": 70.0,
                            "maxwind_mph": 9.4,
                            "maxwind_kph": 15.1,
                            "totalprecip_mm": 0.2,
                            "totalprecip_in": 0.01,
                            "totalsnow_cm": 0.0,
                            "avgvis_km": 10.0,
                            "avgvis_miles": 6.0,
                            "avghumidity": 64.0,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": 83,
                            "daily_will_it_snow": 0,
                            "daily_chance_of_snow": 0,
                            "condition": {
                                "text": "Patchy rain possible",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                                "code": 1063
                            },
                            "uv": 5.0
                        },
                        "astro": {
                            "sunrise": "05:38 AM",
                            "sunset": "08:33 PM",
                            "moonrise": "No moonrise",
                            "moonset": "05:06 PM",
                            "moon_phase": "Waning Crescent",
                            "moon_illumination": "34",
                            "is_moon_up": 1,
                            "is_sun_up": 0
                        },
                        "hour": [
                            {
                                "time_epoch": 1691622000,
                                "time": "2023-08-10 00:00",
                                "temp_c": 17.3,
                                "temp_f": 1,

                            },
                            {
                                "time_epoch": 1691625600,
                                "time": "2023-08-10 01:00",
                                "temp_c": 16.9,
                                "temp_f": 2,

                            },
                            {
                                "time_epoch": 1691629200,
                                "time": "2023-08-10 02:00",
                                "temp_c": 16.7,
                                "temp_f": 3,

                            },
                            {
                                "time_epoch": 1691632800,
                                "time": "2023-08-10 03:00",
                                "temp_c": 16.4,
                                "temp_f": 4,

                            },
                            {
                                "time_epoch": 1691636400,
                                "time": "2023-08-10 04:00",
                                "temp_c": 16.1,
                                "temp_f": 5,

                            },
                            {
                                "time_epoch": 1691640000,
                                "time": "2023-08-10 05:00",
                                "temp_c": 16.0,
                                "temp_f": 6,

                            },
                            {
                                "time_epoch": 1691643600,
                                "time": "2023-08-10 06:00",
                                "temp_c": 16.7,
                                "temp_f": 7,

                            },
                            {
                                "time_epoch": 1691647200,
                                "time": "2023-08-10 07:00",
                                "temp_c": 18.4,
                                "temp_f": 8,

                            },
                            {
                                "time_epoch": 1691650800,
                                "time": "2023-08-10 08:00",
                                "temp_c": 19.9,
                                "temp_f": 9,

                            },
                            {
                                "time_epoch": 1691654400,
                                "time": "2023-08-10 09:00",
                                "temp_c": 21.4,
                                "temp_f": 10,

                            },
                            {
                                "time_epoch": 1691658000,
                                "time": "2023-08-10 10:00",
                                "temp_c": 23.1,
                                "temp_f": 11,

                            },
                            {
                                "time_epoch": 1691661600,
                                "time": "2023-08-10 11:00",
                                "temp_c": 24.5,
                                "temp_f": 12,

                            },
                            {
                                "time_epoch": 1691665200,
                                "time": "2023-08-10 12:00",
                                "temp_c": 25.8,
                                "temp_f": 13,

                            },
                            {
                                "time_epoch": 1691668800,
                                "time": "2023-08-10 13:00",
                                "temp_c": 26.3,
                                "temp_f": 14},

                            {
                                "time_epoch": 1691672400,
                                "time": "2023-08-10 14:00",
                                "temp_c": 26.2,
                                "temp_f": 15,
                            },
                            {
                                "time_epoch": 1691676000,
                                "time": "2023-08-10 15:00",
                                "temp_c": 26.1,
                                "temp_f": 16,

                            },
                            {
                                "time_epoch": 1691679600,
                                "time": "2023-08-10 16:00",
                                "temp_c": 26.2,
                                "temp_f": 17,

                            },
                            {
                                "time_epoch": 1691683200,
                                "time": "2023-08-10 17:00",
                                "temp_c": 25.4,
                                "temp_f": 18,

                            },
                            {
                                "time_epoch": 1691686800,
                                "time": "2023-08-10 18:00",
                                "temp_c": 24.3,
                                "temp_f": 19,

                            },
                            {
                                "time_epoch": 1691690400,
                                "time": "2023-08-10 19:00",
                                "temp_c": 22.8,
                                "temp_f": 20,

                            },
                            {
                                "time_epoch": 1691694000,
                                "time": "2023-08-10 20:00",
                                "temp_c": 21.3,
                                "temp_f": 21,

                            },
                            {
                                "time_epoch": 1691697600,
                                "time": "2023-08-10 21:00",
                                "temp_c": 20.4,
                                "temp_f": 22,

                            },
                            {
                                "time_epoch": 1691701200,
                                "time": "2023-08-10 22:00",
                                "temp_c": 19.6,
                                "temp_f": 23,

                            },
                            {
                                "time_epoch": 1691704800,
                                "time": "2023-08-10 23:00",
                                "temp_c": 19.0,
                                "temp_f": 24,

                            }
                        ]
                    }
                ]
            }
        }

        api_service = APIService("test_loc")
        cleaned_data = api_service.clean_data(mock_response)

        correct = {"location": {
            "name": "loc",
            "region": "loc, loc",
            "country": "UK",
        },
            "current": {
                "temp_f": 73.4,
                "condition": "Partly cloudy",
                "wind_mph": 9.4,
            },
            "forecast": {
                "max_temp": 79.3,
                "min_temp": 60.8,
                "avg_temp": 70.0,

                "daily_chance_of_rain": 83,
                "hourly_temp": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
            }
        }

        self.assertEqual(cleaned_data, correct)


if __name__ == '__main__':
    unittest.main()
