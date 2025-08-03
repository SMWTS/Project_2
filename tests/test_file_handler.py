from src.file_handler import FileHandler
from src.vacancy import Vacancy


class DummyHandler(FileHandler):
    def __init__(self):
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)

    def get_vacancies(self):
        return self.vacancies

    def delete_vacancy(self, vacancy):
        self.vacancies = [v for v in self.vacancies if v.url != vacancy.url]


def test_filehandler_methods():
    handler = DummyHandler()
    v = Vacancy("Test", "http://url", 1000, "desc")
    handler.add_vacancy(v)
    assert v in handler.get_vacancies()
    handler.delete_vacancy(v)
    assert v not in handler.get_vacancies()
