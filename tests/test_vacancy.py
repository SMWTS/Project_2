
from src.vacancy import Vacancy


def test_vacancy_creation():
    v = Vacancy("Test", "http://test", 50000, "desc")
    assert v.name == "Test"
    assert v.url == "http://test"
    assert v.salary == 50000
    assert v.description == "desc"


def test_to_dict():
    v = Vacancy("Test", "http://test", 12345, "desc")
    d = v.to_dict()
    assert isinstance(d, dict)
    assert d["name"] == "Test"
    assert d["url"] == "http://test"
    assert d["salary"] == 12345
    assert d["description"] == "desc"
