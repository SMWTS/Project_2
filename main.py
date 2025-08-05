from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_handler import JSONHandler
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies

def user_interaction():
    """
        Основной цикл взаимодействия с пользователем.
    """
    api = HeadHunterAPI()
    storage = JSONHandler()

    while True:
        print("\nВыберите действие:")
        print("1. Поиск вакансий по ключевому слову")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Фильтрация вакансий по ключевым словам")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            search_query = input("Введите поисковый запрос: ")
            raw_data = api.get_vacancies(search_query)
            vacancies = Vacancy.cast_to_object_list(raw_data)
            for v in vacancies:
                storage.add_vacancy(v)
            print(f"Добавлено {len(vacancies)} вакансий.")
        elif choice == '2':
            n = int(input("Введите количество вакансий для вывода: "))
            all_vacancies = storage.get_vacancies()
            sorted_vacancies = sort_vacancies(all_vacancies)
            print_vacancies(get_top_vacancies(sorted_vacancies, n))
        elif choice == '3':
            keywords = input("Введите ключевые слова через запятую: ").split(',')
            all_vacancies = storage.get_vacancies()
            filtered = filter_vacancies(all_vacancies, keywords)
            print_vacancies(filtered)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод.")

if __name__ == "__main__":
    user_interaction()
