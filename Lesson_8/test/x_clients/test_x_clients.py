import pytest
import requests
from pages.Employee import Employer
from constants import X_client_URL


def test_authorization(get_token):
    token, code = get_token
    """Удостоверяемся, что токен не пустой"""
    assert token is not None
    """Проверяем, что код ответа сервера == 201"""
    assert code == 201
    """Удостоверяемся, что токен имеет строковый формат"""
    assert isinstance(token, str)


def test_getcompany_id(get_list_companies):
    company_id = get_list_companies
    """Удостоверяемся, что ID не пустой"""
    assert company_id is not None
    """Проверяем, что ID компании состоит только из цифр"""
    assert str(company_id).isdigit()


def test_add_employer(add_new_employer):  # Новый сотрудник создан в фикстуре
    """Получаем ID работника"""
    new_employer_id = add_new_employer[0]
    """Получаем заголовки запроса"""
    new_employer_headers = add_new_employer[1]
    """Удостоверяемся, что ID этого сотрудника не пустой"""
    assert new_employer_id is not None
    """Проверяем, что заголовки не пустые"""
    assert new_employer_headers is not None


"""Проверяем невозможность создания клиента без токена и тела запроса"""


def test_add_employer_without_token_and_body():
    headers = {}
    body_employer = {}
    resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer)
    message = resp_add_new_employer.json()['message']
    code = resp_add_new_employer.status_code
    assert message == 'Unauthorized'
    assert code == 401


def test_get_employer(get_list_companies):
    employer = Employer()
    company_id = get_list_companies
    """Получаем список работников конкретной компании"""
    list_employers = employer.get_list_employers(company_id)
    """Проверяем, что нам вернулся список [], а не строка, число или др. тип"""
    assert isinstance(list_employers[0], list)
    """Проверяем, что код ответа == 200"""
    assert list_employers[1] == 200
    """Проверяем, что параметры ID компании в запросе не пустые"""
    assert list_employers[2] is not None


"""Проверяем, обязательное поле 'ID компании' в запросе на получение списка работников - без ID компании"""


def test_get_list_employers_missing_company_id():
    employer = Employer()
    try:
        employer.get_list_employers()
    except TypeError as e:
        assert str(e) == "Employer.get_list_employers() missing 1 required positional argument: 'company_id'"


"""Проверяем, обязательное поле 'ID компании' в запросе на получение списка работников - не валидное ID компании(пустая строка)"""


def test_get_list_employers_invalid_company_id():
    employer = Employer()
    try:
        employer.get_list_employers('')
    except TypeError as e:
        assert str(e) == "Employer.get_list_employers() missing 1 required positional argument: 'company_id'"


def test_get_info_new_employer(add_new_employer):
    employer = Employer()
    id_new_employer = add_new_employer[0]
    """Получаем информацию о добавленном сотруднике"""
    info = employer.get_new_employer(id_new_employer)
    """Сравниваем ID сотрудника из полученной информации c ID сотрудника, которое появилось при создании сотрудника"""
    assert info[1] == id_new_employer
    """Проверяем, что код ответа == 200"""
    assert info[2] == 200


"""Проверяем, обязательное поле 'ID сотрудника' в запросе на получение информации о сотрудника - без ID сотрудника"""


def test_get_info_new_employers_missing_employer_id():
    employer = Employer()
    try:
        employer.get_new_employer()
    except TypeError as e:
        assert str(e) == "Employer.get_new_employer() missing 1 required positional argument: 'id_new_employer'"


def test_change(add_new_employer, get_token):
    employer = Employer()
    id_new_employer = add_new_employer[0]
    token = get_token[0]
    response = employer.change_new_employer(id_new_employer, token)
    """Проверяем, что ID сотрудника соответствует ID при создании сотрудника"""
    assert response[0] == id_new_employer
    """Проверяем, что тело в запрос ушло не пустое"""
    assert response[1] is not None


"""Проверяем, обязательное поле 'ID сотрудника' и 'token' в запросе на изменение информации о сотруднике - без ID сотрудника и токена"""


def test_employers_missing_id_and_token():
    employer = Employer()
    try:
        employer.change_new_employer()
    except TypeError as e:
        assert str(
            e) == "Employer.change_new_employer() missing 2 required positional arguments: 'id_new_employer' and 'token'"


def test_changed_employer():
    employer = Employer()
    changed = employer.get_new_employer_changed()
    """Проверяем, что измененное значение фамилии, соответствует заданному"""
    assert changed[1] == 'Pupkin'
    """Проверяем, что измененное значение почты, соответствует заданному"""
    assert changed[2] == 'test2@mail.ru'
