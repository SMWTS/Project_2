from src.api import HeadHunterAPI


def test_get_vacancies_returns_list():
    api = HeadHunterAPI()
    result = api.get_vacancies("разработчик")
    assert isinstance(result, list)
    if result:
        # Проверка, что элементы — словари с ключами
        for item in result:
            assert isinstance(item, dict)
            assert "name" in item
            assert "url" in item
