import requests
import json
import allure
from Lesson_9.conftest import url

path = '/employee/'

class Employer:
    def __init__(self, url=url):
        self.url = url

    @allure.step("Получаем список сотрудников компании по id компании")    
    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()

    @allure.step("Добавляем сотрудника в компанию")
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        # print(response.json())
        return response.json()

    @allure.step("Получаем информацию о сотруднике по его ID")
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response

    @allure.step("Обновляем данные о сотруднике")
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(employee_id), headers=headers,
                                  json=body)
        return response
