def filter_vacancies(vacancies: list, keywords: list) -> list:
    """
    Фильтрует вакансии по ключевым словам в описании.

    :param vacancies: Список вакансий.
    :param keywords: Список ключевых слов.
    :return: Отфильтрованный список вакансий.
    """
    return [v for v in vacancies if any(keyword.lower() in v.description.lower() for keyword in keywords)]


def get_vacancies_by_salary(vacancies: list, min_salary: int, max_salary: int) -> list:
    """
    Фильтрует вакансии по диапазону зарплат.

    :param vacancies: Список вакансий.
    :param min_salary: Минимальная зарплата.
    :param max_salary: Максимальная зарплата.
    :return: Отфильтрованный список вакансий.
    """
    return [v for v in vacancies if min_salary <= v.salary <= max_salary]


def sort_vacancies(vacancies: list) -> list:
    """
    Сортирует вакансии по зарплате по убыванию.

    :param vacancies: Список вакансий.
    :return: Отсортированный список.
    """
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: list, n: int) -> list:
    """
    Возвращает топ N вакансий.

    :param vacancies: Список вакансий.
    :param n: Количество вакансий.
    :return: Топ N вакансий.
    """
    return vacancies[:n]


def print_vacancies(vacancies: list):
    """
    Выводит список вакансий.

    :param vacancies: Список вакансий.
    """
    for v in vacancies:
        print(f"Название: {v.name}")
        print(f"Ссылка: {v.url}")
        print(f"Зарплата: {v.salary}")
        print(f"Описание: {v.description}")
        print("-" * 50)
