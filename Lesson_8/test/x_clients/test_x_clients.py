import pytest
# from pages.Autorization import InsertLogpass
# from pages.Company import GetCompany
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


def test_get_employer():
    employer = Employer(Employer)
    """Получаем список работников конкретной компании"""
    list = employer.get_list_employers()[0]
    print(list)

    # list_company = employer.get_list_employers()[0]
    # """Получаем код ответа сервера"""
    # xcode = employer.get_list_employers()[1]
    # """Проверяем, что нам вернулся список [], а не строка, число или др. тип"""
    # assert isinstance(list_company, list)
    # """Проверяем, что код ответа == 200"""
    # assert xcode == 200
    # """Проверяем, что параметры с ID компании не пустые"""
    # assert employer.get_list_employers()[2] is not None

    #
    #
    # def test_add_employer():
    #     employer = Employer(Employer)
    #     """Добавляем сотрудника в конкретную компанию"""
    #     new_employer = employer.add_new_employer()
    #     """Удостоверяемся, что ID этого сотрудника не пустой"""
    #     assert new_employer[0] is not None
    #     """Проверяем, что заголовки не пустые"""
    #     assert new_employer[1] is not None
    #     # print(new_employer)
    #     # print(new_employer[0])
    #
    #
    # def test_get_info_new_employer():
    #     employer = Employer(Employer)
    #     """Получаем информацию о добавленном сотруднике"""
    #     info = employer.get_new_employer()
    #     print(info)

    """Проверяем, что код ответа == 200"""
    # assert info_id[2] == 200

# """Изменяем данные сотрудника"""
# employer.test_change_new_employer()
# """Получаем данные по измененному сотруднику"""
# employer.test_get_new_employer_changed()
