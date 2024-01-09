import pytest
import sys
sys.path.append('/home/evgen/Documents/Automation-Python/Lesson_9')
from pages.Employee import Employer
from pages.DataBase import DataBase
import allure

api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com/x_clients")


@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, после чего сравниваем их")
@allure.feature('Тест 1')
def test_get_list_of_employers():
    with allure.step("БД - Создаем компанию"):
        db.create_company_db('Evgen testers', 'cool_company')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.get_max_id()
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.db_create_employer(max_id, "Evgen", "Voronov", 8002000600)
    with allure.step("БД - Получаем список сотрудников из последней созданной компании"):
        db_employer_list = db.db_get_list_employer(max_id)
    with allure.step("API - Получаем список сотрудников из последней созданной компании"):
        api_employer_list = api.get_list_employers(max_id)
    with allure.step("Сравниваем списки сотрудников полученных ид БД и через API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete_company(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудников")
@allure.description("Добавляем сотрудника в БД и сравниваем с АПИ имя, статус и фамилию")
@allure.feature('Тест 2')
def test_add_new_employer():
    db.create_company_db('Evgen adding new employer', 'employer')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Evgen", "Voronov", 8002000600)
    resp = api.get_list_employers(max_id)
    employer_id = resp[0]["id"]
    """Сравниваем ID компании"""
    assert resp[0]["companyId"] == max_id
    """Сравниваем имя сотрудника с заданным"""
    assert resp[0]["firstName"] == "Evgen"
    """Удостоверяемся что статус сотрудника - True"""
    assert resp[0]["isActive"] == True
    """Сравниваем фамилию сотрудника с заданной"""
    assert resp[0]["lastName"] == "Voronov"
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employer(employer_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete_company(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='trivial')
@allure.title("Получение информации о сотруднике по ID")
@allure.description("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника в БД")
@allure.feature('Тест 3')
def test_get_employer_by_id():
    db.create_company_db('Employer get id company', 'new')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Evgen", "Voronov", 8002000600)
    employer_id = db.db_get_employer_id(max_id)
    """Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника в БД"""
    get_info = api.get_employer_by_id(employer_id)
    assert get_info["firstName"] == "Evgen"
    assert get_info["lastName"] == "Voronov"
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employer(employer_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete_company(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Обновление информации о сотруднике")
@allure.description("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике")
@allure.feature('Тест 4')
def test_update_user_info():
    db.create_company_db('New updating company', 'test')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Evgen", "Voronov", 8002000600)
    employer_id = db.db_get_employer_id(max_id)
    db.update_employer_info("King", employer_id)
    """Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике"""
    get_info = api.get_employer_by_id(employer_id)
    assert get_info["firstName"] == "King"
    assert get_info["lastName"] == "Voronov"
    assert get_info["isActive"] == True
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employer(employer_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete_company(max_id)
