import pytest
from pages.Autorization import InsertLogpass
from pages.Company import GetCompany
from pages.Employee import Employer


def test_employer():
    """Получаем токен"""
    x_client_token = InsertLogpass(InsertLogpass)
    x_client_token.test_get_token()
    """Получаем  ID компании, последней из списка"""
    company_id = GetCompany(GetCompany)
    company_id.test_get_list_companies()

    employer = Employer(Employer)
    """Получаем список работников конкретной компании"""
    employer.test_get_list_employers()
    """Добавляем сотрудника в конкретную компанию"""
    employer.test_add_new_employer()
    """Получаем информацию о добавленном сотруднике"""
    employer.test_get_new_employer()
    """Изменяем данные сотрудника"""
    employer.test_change_new_employer()
    """Получаем данные по измененному сотруднику"""
    employer.test_get_new_employer_changed()
