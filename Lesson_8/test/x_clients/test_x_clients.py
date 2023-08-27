import pytest
from pages.Employee import Employer


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


def test_get_employer():
    employer = Employer(Employer)
    """Получаем список работников конкретной компании"""
    list = employer.get_list_employers()[0]
    """Получаем код ответа сервера"""
    xcode = employer.get_list_employers()[1]
    """Проверяем, что нам вернулся список [], а не строка, число или др. тип"""
    assert isinstance(list, list)
    """Проверяем, что код ответа == 200"""
    assert xcode == 200
    """Проверяем, что параметры ID компании в запросе не пустые"""
    assert employer.get_list_employers()[2] is not None


@pytest.mark.skip()
def test_get_info_new_employer(add_new_employer):
    employer = Employer(Employer)
    id_add = add_new_employer[0]
    """Получаем информацию о добавленном сотруднике"""
    info = employer.get_new_employer()
    """Сравниваем ID сотрудника из полученной информации c ID сотрудника, которое появилось при создании сотрудника"""
    assert info[1] == id_add
    """Проверяем, что код ответа == 200"""
    assert info[2] == 200


@pytest.mark.skip()
def test_change(add_new_employer):
    id_add = add_new_employer[0]
    employer = Employer(Employer)
    """Проверяем, что ID сотрудника соответствует ID при создании сотрудника"""
    assert employer.change_new_employer()[0] == id_add
    """Проверяем, что тело в запрос ушло не пустое"""
    assert employer.change_new_employer()[1] is not None


@pytest.mark.skip()
def test_changed_employer():
    employer = Employer(Employer)
    """Проверяем, что измененное значение фамилии, соответствует заданному"""
    assert employer.get_new_employer_changed()[1] == 'Pupkin'
    """Проверяем, что измененное значение почты, соответствует заданному"""
    assert employer.get_new_employer_changed()[2] == 'test2@mail.ru'
