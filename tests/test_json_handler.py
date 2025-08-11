import json

import pytest

from src.json_handler import JSONHandler
from src.vacancy import Vacancy


@pytest.fixture
def temp_json_file(tmp_path):
    file_path = tmp_path / "vacancies_test.json"
    return str(file_path)


def test_add_get_delete_vacancy(tmp_path, temp_json_file):
    handler = JSONHandler(temp_json_file)
    v = Vacancy("Test", "http://url", 1000, "desc")
    # Добавление
    handler.add_vacancy(v)
    vacancies = handler.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].url == "http://url"
    # Удаление
    handler.delete_vacancy(v)
    vacancies = handler.get_vacancies()
    assert len(vacancies) == 0
    # Проверка файла
    with open(temp_json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data == []


def test_duplicate_addition(tmp_path, temp_json_file):
    handler = JSONHandler(temp_json_file)
    v = Vacancy("Test", "http://url", 1000, "desc")
    handler.add_vacancy(v)
    handler.add_vacancy(v)  # повторное добавление
    vacancies = handler.get_vacancies()
    assert len(vacancies) == 1
