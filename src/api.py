from abc import ABC, abstractmethod

import requests


class APIBase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass


class HeadHunterAPI(APIBase):
    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__session = requests.Session()

    def __connect(self):
        response = self.__session.get(self.__base_url)
        if response.status_code != 200:
            raise ConnectionError(f"API connection failed with status {response.status_code}")

    def get_vacancies(self, search_query: str):
        self.__connect()
        params = {"text": search_query, "per_page": 50}
        response = self.__session.get(self.__base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("items", [])
        else:
            return []
