from heart_rate_bot import __version__
from heart_rate_bot.math import calculate_heart_rate


def test_version():
    assert __version__ == "0.1.0"


def test_calculate_heart_rate():
    result = calculate_heart_rate(45, 80)
    assert result == (146.5, 160.75)
