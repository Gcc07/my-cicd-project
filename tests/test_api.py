import pytest
import requests

# Apply multiple markers to one test


@pytest.mark.external
@pytest.mark.slow
def test_weather_api():
    WEATHER_URL = "https://api.weather.gov"
    resp = requests.get(WEATHER_URL)
    assert resp.status_code == 200