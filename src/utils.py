from typing import List


def filter_vacancies(vacancies: List, keywords: List[str]) -> List:
    return [v for v in vacancies if any(keyword.lower() in v.description.lower() for keyword in keywords)]


def get_vacancies_by_salary(vacancies: List, min_salary: int, max_salary: int) -> List:
    return [v for v in vacancies if min_salary <= v.salary <= max_salary]


def sort_vacancies(vacancies: List) -> List:
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List, n: int) -> List:
    return vacancies[:n]


def print_vacancies(vacancies: List):
    for v in vacancies:
        print(f"Название: {v.name}")
        print(f"Ссылка: {v.url}")
        print(f"Зарплата: {v.salary}")
        print(f"Описание: {v.description}")
        print("-" * 50)
