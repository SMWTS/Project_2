import json

from src.file_handler import FileHandler
from src.vacancy import Vacancy


class JSONHandler(FileHandler):
    """
    Класс для работы с JSON-файлом хранения вакансий.
    """

    def __init__(self, filename: str = "vacancies.json"):
        """
        Инициализация обработчика файла."""

        self.__filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавляет вакансию в файл, избегая дублирования."""

        data = self.get_vacancies()
        # Проверка на дубли
        if any(v.url == vacancy.url for v in data):
            return
        data.append(vacancy)
        self._save(data)

    def get_vacancies(self) -> list[Vacancy]:
        """
        Получает список вакансий из файла."""

        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                raw = json.load(f)
            return [Vacancy(**v) for v in raw]
        except FileNotFoundError:
            return []

    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удаляет вакансию по URL."""

        data = self.get_vacancies()
        data = [v for v in data if v.url != vacancy.url]
        self._save(data)

    def _save(self, vacancies: list[Vacancy]):
        """
        Сохраняет список вакансий в файл."""

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in vacancies], f, ensure_ascii=False, indent=4)
