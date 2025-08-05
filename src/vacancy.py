from typing import Any


class Vacancy:
    """
    Класс для представления вакансии.
    Использует __slots__ для ограничения атрибутов.
    """

    __slots__ = ["name", "url", "salary", "description"]

    def __init__(self, name: str, url: str, salary: Any, description: str):
        """
        Инициализация объекта Vacancy.
        """

        self.name = name
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.description = description

    def __validate_salary(self, salary):
        """
        Валидирует и возвращает зарплату."""

        if salary is None:
            return 0
        if isinstance(salary, dict):
            return salary.get("from", 0)
        if isinstance(salary, (int, float)):
            return salary
        return 0

    def __lt__(self, other):
        """
        Меньше по зарплате."""

        return self.salary < other.salary

    def __eq__(self, other):
        """
        Равно по зарплате."""

        if not isinstance(other, Vacancy):
            return NotImplemented
        return (
            self.name == other.name
            and self.url == other.url
            and self.salary == other.salary
            and self.description == other.description
        )

    def __hash__(self):
        return hash((self.name, self.url, self.salary, self.description))

    @classmethod
    def cast_to_object_list(cls, data: list):
        """
        Преобразует список словарей в список объектов Vacancy."""

        return [cls(v["name"], v["url"], v.get("salary"), v.get("description", "")) for v in data]

    def to_dict(self):
        """
        Преобразует объект в словарь для сериализации."""

        return {"name": self.name, "url": self.url, "salary": self.salary, "description": self.description}
