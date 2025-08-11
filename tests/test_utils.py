from src.utils import filter_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies
from src.vacancy import Vacancy


def test_filter_vacancies():
    v1 = Vacancy("A", "url1", 1000, "Python developer")
    v2 = Vacancy("B", "url2", 2000, "Java developer")
    vacancies = [v1, v2]
    filtered = filter_vacancies(vacancies, ["python"])
    assert v1 in filtered
    assert v2 not in filtered


def test_get_vacancies_by_salary():
    v1 = Vacancy("A", "url1", 1000, "")
    v2 = Vacancy("B", "url2", 3000, "")
    vacancies = [v1, v2]
    result = get_vacancies_by_salary(vacancies, 500, 2000)
    assert v1 in result
    assert v2 not in result


def test_sort_vacancies():
    v1 = Vacancy("A", "url1", 1000, "")
    v2 = Vacancy("B", "url2", 3000, "")
    sorted_list = sort_vacancies([v1, v2])
    assert sorted_list[0] == v2


def test_print_vacancies(capsys):
    v = Vacancy("A", "url", 1000, "desc")
    print_vacancies([v])
    captured = capsys.readouterr()
    assert "Название" in captured.out
