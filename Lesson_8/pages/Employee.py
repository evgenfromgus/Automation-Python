import requests
from constants import X_client_URL
from data.data import body_employer
from data.data import body_change_employer
from pages.Company import GetCompany
from pages.Autorization import InsertLogpass

puth = '/employee/'


class Employer:
    def __init__(self, url):
        self.url = url

    def test_get_list_employers(self):
        company = GetCompany
        company_id = company.test_get_list_companies(self)
        company = {'company': company_id}
        resp_employers = requests.get(X_client_URL + '/employee', params=company)
        list_employers = resp_employers.json()
        return list_employers

    def test_add_new_employer(self):
        dostup = InsertLogpass
        x_client_token = dostup.test_get_token(self)
        headers = {'x-client-token': x_client_token}
        resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer)
        new_employer_id = resp_add_new_employer.json()['id']
        return new_employer_id

    def test_get_new_employer(self):
        id_employer = str(self.test_add_new_employer())
        resp_get_new_employer = requests.get(X_client_URL + puth + id_employer)
        info_new_employer = resp_get_new_employer.json()
        return info_new_employer

    def test_change_new_employer(self):
        id_employer = str(self.test_add_new_employer())
        dostup = InsertLogpass
        x_client_token = dostup.test_get_token(self)
        headers = {'x-client-token': x_client_token}
        resp_change_employer = requests.patch(X_client_URL + puth + id_employer, headers=headers,
                                              json=body_change_employer)
        inform_changed_employer = resp_change_employer.json()
        return inform_changed_employer

    def test_get_new_employer_changed(self):
        id_employer = str(self.test_add_new_employer())
        resp_new_employer_info_changed = requests.get(X_client_URL + puth + id_employer)
        info_new_employer = resp_new_employer_info_changed.json()
        return info_new_employer
