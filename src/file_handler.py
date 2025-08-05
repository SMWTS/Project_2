from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class FileHandler(ABC):
    """
    Абстрактный базовый класс для обработки файлов, предназначенный для хранения,
    получения и удаления вакансий в файле.
    """

    @abstractmethod
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass
