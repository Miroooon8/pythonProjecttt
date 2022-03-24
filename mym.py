import requests
from enum import Enum


class Units(Enum):
    IM = 'imperic', 'имперская'
    MT = 'metric', 'метрическая'

    @staticmethod
    def get_all():
        return [
            Units.IM,
            Units.MT
        ]


class Lang(Enum):
    RU = 'ru', 'russian', 'русский'
    EN = 'en', 'english', 'английский'
    FR = 'fr', 'french', 'французский'

    @staticmethod
    def get_all():
        return [
            Lang.RU,
            Lang.EN,
            Lang.FR
        ]


class WeatherForecast:
    _token = "c38206202a68eb0e43cea47e806cafb9"
    _url = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self):
        self._city = 'Moscow'
        self._lang = Lang.RU
        self._units = Units.IM

    def _get_params(self):
        return {
            'appid': WeatherForecast._token,
            'units': self._units,
            'lang': self._lang.value[0],
            'q': self._city
        }

    def get_data(self):
        return requests.get(WeatherForecast._url, self._get_params())

    def set_city(self, new_city: str) -> bool:
        prev_city = self._city
        self._city = new_city
        if self.get_data().status_code != 200:
            self._city = prev_city
            return True
        return False

    def set_lang(self, language: str) -> bool:
        for lang in Lang.get_all():
            if language == lang.value[1] or language == lang.value[2]:
                self._lang = lang
                return True
        return False

    def set_lang(self, unit: str) -> bool:
        for u in Units.get_all():
            if unit == Units.value[1] or unit == Units.value[2]:
                self._units = u
                return True
        return False
