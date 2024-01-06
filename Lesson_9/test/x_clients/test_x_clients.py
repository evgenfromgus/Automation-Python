# import pytest
# import allure
import requests
from pages.Employee import Employer
from constants import X_client_URL
from pages.DataBase import DataBase


def test_creating_company(self=None):
    create = DataBase
    """Cоздание компании в БД"""
    company_creating = create.test_db_creating_company(self)
    """Проверяем, через API, что наша компания создалась с заданным именем"""
    param_true = {'active': 'true'}
    resp_companies = requests.get(X_client_URL + '/company', params=param_true)
    last_companies_name = resp_companies.json()[-1]['name']
    assert last_companies_name == "python_db"


def test_get_company_id(self=None):
    create = DataBase
    """Получаем ID созданной компании из БД"""
    get_comp_id = create.test_db_get_id_company(self)
    """Удостоверяемся, что ID не пустой"""
    assert get_comp_id is not None
    """Получаем через API ID созданной компании"""
    param_true = {'active': 'true'}
    resp_companies = requests.get(X_client_URL + '/company', params=param_true)
    last_companies_id = resp_companies.json()[-1]['id']
    """Сравниваем эти ID"""
    assert last_companies_id == get_comp_id


def test_creating_employee(self=None):
    create = DataBase()
    """Создаем сотрудника нашей компании в БД"""
    create_employee = create.test_db_creating_employer()
    """Получаем через API имя сотрудника созданного сотрудника"""
    api_emp = Employer()
    name_api = api_emp.get_new_employer(self)[3]
    """Сравниваем имена сотрудника указанного при создании в БД и полученного через API"""
    assert name_api == 'Ivan!'

#
# def test_add_employer(add_new_employer):  # Новый сотрудник создан в фикстуре
#     """Получаем ID работника"""
#     new_employer_id = add_new_employer[0]
#     """Получаем заголовки запроса"""
#     new_employer_headers = add_new_employer[1]
#     """Удостоверяемся, что ID этого сотрудника не пустой"""
#     assert new_employer_id is not None
#     """Проверяем, что заголовки не пустые"""
#     assert new_employer_headers is not None
#
#
#
# def test_get_employer(get_list_companies):
#     employer = Employer()
#     company_id = get_list_companies
#     """Получаем список работников конкретной компании"""
#     list_employers = employer.get_list_employers(company_id)
#     """Проверяем, что нам вернулся список [], а не строка, число или др. тип"""
#     assert isinstance(list_employers[0], list)
#     """Проверяем, что код ответа == 200"""
#     assert list_employers[1] == 200
#     """Проверяем, что параметры ID компании в запросе не пустые"""
#     assert list_employers[2] is not None
#
#
# """Проверяем, обязательное поле 'ID компании' в запросе на получение списка работников - без ID компании"""
#
#
# def test_get_list_employers_missing_company_id():
#     employer = Employer()
#     try:
#         employer.get_list_employers()
#     except TypeError as e:
#         assert str(e) == "Employer.get_list_employers() missing 1 required positional argument: 'company_id'"
#
#
# """Проверяем, обязательное поле 'ID компании' в запросе на получение списка работников - не валидное ID компании(пустая строка)"""
# def test_get_list_employers_invalid_company_id():
#     employer = Employer()
#     try:
#         employer.get_list_employers('')
#     except TypeError as e:
#         assert str(e) == "Employer.get_list_employers() missing 1 required positional argument: 'company_id'"
#
#
# def test_get_info_new_employer(add_new_employer):
#     employer = Employer()
#     id_new_employer = add_new_employer[0]
#     """Получаем информацию о добавленном сотруднике"""
#     info = employer.get_new_employer(id_new_employer)
#     """Сравниваем ID сотрудника из полученной информации c ID сотрудника, которое появилось при создании сотрудника"""
#     assert info[1] == id_new_employer
#     """Проверяем, что код ответа == 200"""
#     assert info[2] == 200
#
#
# """Проверяем, обязательное поле 'ID сотрудника' в запросе на получение информации о сотрудника - без ID сотрудника"""
# def test_get_info_new_employers_missing_employer_id():
#     employer = Employer()
#     try:
#         employer.get_new_employer()
#     except TypeError as e:
#         assert str(e) == "Employer.get_new_employer() missing 1 required positional argument: 'id_new_employer'"
#
#
# def test_change(add_new_employer, get_token):
#     employer = Employer()
#     id_new_employer = add_new_employer[0]
#     token = get_token[0]
#     response = employer.change_new_employer(id_new_employer, token)
#     """Проверяем, что ID сотрудника соответствует ID при создании сотрудника"""
#     assert response[0] == id_new_employer
#     """Проверяем, что тело в запрос ушло не пустое"""
#     assert response[1] is not None
#
#
# """Проверяем, обязательное поле 'ID сотрудника' и 'token' в запросе на изменение информации о сотруднике - без ID сотрудника и токена"""
# def test_employers_missing_id_and_token():
#     employer = Employer()
#     try:
#         employer.change_new_employer()
#     except TypeError as e:
#         assert str(
#             e) == "Employer.change_new_employer() missing 2 required positional arguments: 'id_new_employer' and 'token'"
#
#
# def test_changed_employer():
#     employer = Employer()
#     changed = employer.get_new_employer_changed()
#     """Проверяем, что измененное значение фамилии, соответствует заданному"""
#     assert changed[1] == 'Pupkin'
#     """Проверяем, что измененное значение почты, соответствует заданному"""
#     assert changed[2] == 'test2@mail.ru'
