import json
from typing import List

from src.file_handler import FileHandler
from src.vacancy import Vacancy


class JSONHandler(FileHandler):
    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        data = self.get_vacancies()
        # Проверка на дубли
        if any(v.url == vacancy.url for v in data):
            return
        data.append(vacancy)
        self._save(data)

    def get_vacancies(self) -> List[Vacancy]:
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                raw = json.load(f)
            return [Vacancy(**v) for v in raw]
        except FileNotFoundError:
            return []

    def delete_vacancy(self, vacancy: Vacancy):
        data = self.get_vacancies()
        data = [v for v in data if v.url != vacancy.url]
        self._save(data)

    def _save(self, vacancies: List[Vacancy]):
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in vacancies], f, ensure_ascii=False, indent=4)
