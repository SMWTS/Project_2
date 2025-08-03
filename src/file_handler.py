from abc import ABC, abstractmethod
from typing import List

from src.vacancy import Vacancy


class FileHandler(ABC):
    @abstractmethod
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass
