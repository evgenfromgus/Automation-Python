import pytest
from Lesson_9.pages.Employee import Employer
from Lesson_9.pages.DataBase import DataBase
import allure

api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com/x_clients")


@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
def test_get_list_of_employees():
    with allure.step("БД - Создаем компанию"):
        db.create('Evgen testers', 'cool_company')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.get_max_id()
    with allure.step("БД - Получаем список сотрудников из последней созданной компании"):
        db_employee_list = db.db_get_list_employee(max_id)
    with allure.step("API - Получаем список сотрудников из последней созданной компании"):
        api_employee_list = api.get_list_employers(max_id)
        print(api_employee_list)
    with allure.step("Сравниваем списки сотрудников полученных ид БД и через API"):
        assert len(db_employee_list) == len(api_employee_list)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete_company(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудников")
def test_add_new_employee():
    db.create('Evgen adding new employee', 'employer')
    max_id = db.get_max_id()
    new_employee = db.db_create_employee(max_id, "Evgen", "Voronov", 8002000600)
    resp = api.get_list_employers(max_id)
    employee_id = resp[0]["id"]
    """Сравниваем ID компании"""
    assert resp[0]["companyId"] == max_id
    """Сравниваем имя сотрудника с заданным"""
    assert resp[0]["firstName"] == "Evgen"
    """Удостоверяемся что статус сотрудника - True"""
    assert resp[0]["isActive"] == True
    """Сравниваем фамилию сотрудника с заданной"""
    assert resp[0]["lastName"] == "Voronov"
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employee(employee_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete_company(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='trivial')
@allure.title("Получение информации о сотруднике по ID")
def test_get_employee_by_id():
    db.create('Employee get id company', 'new')
    max_id = db.get_max_id()
    new_employee = db.db_create_employee(max_id, "Evgen", "Voronov", 8002000600)
    employee_id = db.db_get_employee_id(max_id)
    """Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника в БД"""
    get_info = api.get_employee_by_id(employee_id)
    assert get_info["firstName"] == "Evgen"
    assert get_info["lastName"] == "Voronov"
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employee(employee_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete_company(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Обновление информации о сотруднике")
def test_update_user_info():
    db.create('New updating company', 'test')
    max_id = db.get_max_id()
    new_employee = db.db_create_employee(max_id, "Evgen", "Voronov", 8002000600)
    employee_id = db.db_get_employee_id(max_id)
    db.update_employee_info("King", employee_id)
    """Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике"""
    get_info = api.get_employee_by_id(employee_id)
    assert get_info["firstName"] == "King"
    assert get_info["lastName"] == "Voronov"
    assert get_info["isActive"] == True
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employee(employee_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete_company(max_id)
