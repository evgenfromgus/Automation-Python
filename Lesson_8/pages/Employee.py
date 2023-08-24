import requests
from constants import X_client_URL
from data.data import body_employer
from data.data import body_change_employer
import pytest

# from pages.Company import GetCompany
# from pages.Autorization import InsertLogpass


path = '/employee/'


class Employer:
    def __init__(self, url):
        self.url = url
        # self.id_new_employer = None

    def get_list_employers(self, get_list_companies):
        company_id = get_list_companies
        company = {'company': company_id}
        resp_employers = requests.get(X_client_URL + '/employee', params=company)
        list_employers = resp_employers.json()
        code = resp_employers.status_code
        print(list_employers, code)
        return list_employers, code, company

    # def add_new_employer(self):
    #     headers = {'x-client-token': InsertLogpass.get_token(self)[0]}
    #     resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer)
    #     self.id_new_employer = resp_add_new_employer.json()['id']
    #     return self.id_new_employer, headers
    #
    # def get_new_employer(self):
    #     resp_get_new_employer = requests.get(X_client_URL + path + str(self.id_new_employer))
    #     info_new_employer = resp_get_new_employer.json()
    #     id_new_emp = resp_get_new_employer.json()['id']
    #     # print(id_new_emp)
    #     code = resp_get_new_employer.status_code
    #     return info_new_employer, id_new_emp, code

    # def change_new_employer(self):
    #     # id_employer = str(self.add_new_employer()[0])
    #     headers = {'x-client-token': InsertLogpass.get_token(self)[0]}
    #     resp_change_employer = requests.patch(X_client_URL + path + id_employer, headers=headers,
    #                                           json=body_change_employer)
    #     inform_changed_employer = resp_change_employer.json()
    #     return inform_changed_employer
    #
    # def get_new_employer_changed(self):
    #     # id_employer = str(self.add_new_employer()[0])
    #     resp_new_employer_info_changed = requests.get(X_client_URL + path + id_employer)
    #     info_new_employer = resp_new_employer_info_changed.json()
    #     return info_new_employer
