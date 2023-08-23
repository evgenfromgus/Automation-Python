import pytest
from pages.Autorization import InsertLogpass
from pages.Company import GetCompany
from pages.Employee import Employer


def test_authorization():
    """Получаем токен"""
    x_client_token = InsertLogpass(InsertLogpass)
    xtoken = x_client_token.test_get_token()[0]
    """Получаем код ответа сервера"""
    xcode = x_client_token.test_get_token()[1]
    """Удостоверяемся, что токен не пустой"""
    assert xtoken is not None
    """Удостоверяемся, что токен имеет строковый формат"""
    assert isinstance(xtoken, str)
    """Проверяем, что код ответа сервера == 201"""
    assert xcode == 201


def test_getcompany_id():
    """Получаем ID компании, последней из списка"""
    company_id = GetCompany(GetCompany)
    company_id = company_id.test_get_list_companies()
    """Удостоверяемся, что ID не пустой"""
    assert company_id is not None
    """Проверяем, что ID компании состоит только из цифр"""
    assert str(company_id).isdigit()


def test_get_employer():
    employer = Employer(Employer)
    """Получаем список работников конкретной компании"""
    list_company = employer.test_get_list_employers()[0]
    """Получаем код ответа сервера"""
    xcode = employer.test_get_list_employers()[1]
    """Проверяем, что нам вернулся список [], а не строка, число или др. тип"""
    assert isinstance(list_company, list)
    """Проверяем, что код ответа == 200"""
    assert xcode == 200
    """Проверяем, что параметры с ID компании не пустые"""
    assert employer.test_get_list_employers()[2] is not None


# @pytest.fixture()
def test_add_employer():
    employer = Employer(Employer)
    """Добавляем сотрудника в конкретную компанию"""
    new_employer = employer.test_add_new_employer()
    """Удостоверяемся, что ID этого сотрудника не пустой"""
    assert new_employer[0] is not None
    """Проверяем, что заголовки не пустые"""
    assert new_employer[1] is not None
    print(new_employer)
    print(new_employer[0])

# def test_get_info_new_employer():
#     employer = Employer(Employer)
#     """Получаем информацию о добавленном сотруднике"""
#     info_id = employer.test_get_new_employer()[1]
#     print(info_id)
#     # assert info_id ==

#     # """Получаем ID этого сотрудника"""
#     # id_new_employer_2 = employer.test_get_new_employer()[1]
#     # """Получаем код ответа сервера"""
#     # xcode = employer.test_get_new_employer()[2]
#     """Сравниваем ID этого сотрудника с ID из теста по добавлению сотрудника, чтобы убедиться, что отображается верная информация"""
#     print(info_id[1])
#     # print(test_add_employer[0])
#     # assert info_id[1] == test_add_employer[0]
#     # """Проверяем, что код ответа == 200"""
#     # assert info_id[2] == 200

# """Изменяем данные сотрудника"""
# employer.test_change_new_employer()
# """Получаем данные по измененному сотруднику"""
# employer.test_get_new_employer_changed()
